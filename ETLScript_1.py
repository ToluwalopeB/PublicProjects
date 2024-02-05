import pandas as pd 
from bs4 import BeautifulSoup
from datetime import datetime as dt
import numpy as np 
import sqlite3
import requests



def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp = dt.now().strftime('%c')
    with open (log_file,'a') as file:
        file.write(timestamp+' : '+message+'\n')

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    df = pd.DataFrame(columns = table_attribs)
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page,'html.parser')
    tables = data.find_all('table')
    final_table = [t for t in tables if str(t).find('Market cap<br/>(US$ billion)') > 0]
    rows = final_table[0].find('tbody').find_all('tr')
    for r in rows:
        columns = r.find_all('td')
        # ensure the row is not empty 
        if len(columns) > 1:
            '''
            The bank name is in the 2nd column position [1]
            The content list of that column tag has 4 elements in it
            the element in position[2] has the bank name. The bank name is 
            the tag attribute title it is also the text in the anchor
            tag in contents[2] so the code could have been
            columns[1].contents[2].text

            The market cap is the 3 column (columns[2] we then strip the
            new line from it and cast to a float)
            '''
            dict = {'Name':columns[1].contents[2]['title'],
                    'MC_USD_Billion':float(columns[2].text.strip('\n'))}
            df1 = pd.DataFrame(dict,index = [0])
            df = pd.concat([df,df1],ignore_index=True)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    exchange_rate = pd.read_csv(csv_path)
    ''' to_dict default setting takes the index of the data frame as the 
    key so we det the index of the data frame to currency so that currency values
    will be the key. The result dictionary is a dictionary of dictonaries where each column header in
    the dataframe is a key and the records for that column are stored as a single dictionary with key
    value set as the row index for each record. Selecting [Rate] key gives us the dictionary of exchnage
    rates which is what we need'''
    exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name,sql_connection,if_exists = 'replace', index = False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    query_output = pd.read_sql(query_statement,sql_connection)
    print('query statement: ',query_statement,'\n')
    print('query output: ','\n',query_output,'\n\n')


''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''



url = 'https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name','MC_USD_Billion']
db_name = 'Banks.db'
table_name = 'Largest_banks'
output_path = 'Largest_banks_data.csv'
csv_path = 'exchange_rate.csv'
log_file = 'code_log.txt'


log_progress('Preliminaries complete. Initiating ETL process')

e = extract(url, table_attribs)

log_progress('Data extraction complete. Initiating Transformation process')

t = transform(e,csv_path)

log_progress('Data transformation complete. Initiating Loading process')

x = load_to_csv(t, output_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(db_name)

log_progress('SQL Connection initiated')

y = load_to_db(t, sql_connection, table_name)

log_progress('Data loaded to Database as a table, Executing queries')

q1 = run_query('SELECT * FROM Largest_banks',sql_connection)
q2 = run_query('SELECT AVG(MC_GBP_Billion) FROM Largest_banks',sql_connection)
q3 = run_query('SELECT Name from Largest_banks LIMIT 5',sql_connection)

log_progress('Process Complete')

sql_connection.close()

log_progress('Server Connection closed')

