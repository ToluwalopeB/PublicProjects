import requests
from bs4 import BeautifulSoup
import pandas as pd 
import sqlite3
import numpy as np 
from datetime import datetime



def extract(url, table_attribs):
    ''' This function extracts the required
    information from the website and saves it to a dataframe. The
    function returns the dataframe for further processing. '''
    df = pd.DataFrame(columns = table_attribs)
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page,'html.parser')
    #create a list of all table tags
    tables = data.find_all('table')

    '''
    The GDP table is the  one labelled "GDP (USD million) by country"
    so the list comp below selects just that table body
    into the list final table
    '''
     
    final_table = [t for t in tables if str(t).find('GDP (USD million) by country') > 0]
    '''
    first call find() on the first and only implement in final table
    which is the table tag for the table we're interested in plus all
    its child tag. The result of this is the tbody tag of that table plus
    all its child tags. We then call find_all on the tbody tag to get
    all the row tags as a list. 

    Alternatively we can write the code below as
    rows = final_table[0].find_all('tbody')[0].find_all('tr')
    
    note: find and final cannot be called on a list or list-like
    object so the code below would be wrong. The result of 
    final_table[0].find_all('tbody') is a result set and as 
    such behaves like a list so cannot be used to call
    find_call('tr')

    rows = final_table[0].find_all('tbody').find_all('tr')

    '''
    rows = final_table[0].find('tbody').find_all('tr')
    
    #get rows
    for r in rows:
        column = r.find_all('td')
        # check if row is empty
        if len(column) > 0:
            #confirm column 1 has a link
            column_1 = column[0].find_all('a')
            # create a record if gdp is not missing amd col1 is a link
            if len(column_1)> 0 and column[2].text != '—':
                dict = {'Country':column_1[0].text,'GDP_USD_millions':column[2].text}
                df1 = pd.DataFrame(dict, index = [0])
                df = pd.concat([df,df1],ignore_index = True)
    
    return df


def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of GDP from
    USD (Millions) to USD (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''

    # convert column to list
    temp_list =  df['GDP_USD_millions'].tolist()
    temp_list = [value.split(",") for value in temp_list]
    temp_list = [float(''.join(value)) for value in temp_list]
    temp_list = [np.round(value/1000, decimals=2) for value in temp_list]
    df['GDP_USD_millions'] = temp_list
    df.rename(columns = {'GDP_USD_millions':'GDP_USD_billions'}, inplace = True) 
    return df
    
def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe as a database table
    with the provided name. Function returns nothing.'''
    df.to_sql(table_name,sql_connection, if_exists = 'replace',index = False)

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    final_df = pd.read_sql(query_statement,sql_connection)
    print(final_df.head())


def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''
    ''' Here, you define the required entities and call the relevant 
    functions in the correct order to complete the project. Note that this
    portion is not inside any function.'''
    
    log_time = datetime.now().strftime('%c')
    with open (log_file,'a') as file:
        file.write(log_time+': '+message+'\n')


log_file = "log_file.txt" 

log_progress('Begin ETL')

log_progress('Begin initialization')

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ['Country','GDP_USD_millions']
db_name = 'World_Economies.db'
table_name = 'Countries_by_GDP'
csv_path = 'Countries_by_GDP.csv'
sql_connection = sqlite3.connect(db_name)

log_progress('End initialization')

log_progress('Begin data extraction')

e = extract(url, table_attribs)

log_progress('End data extraction')

log_progress('Begin data transformation')

t = transform(e)

log_progress('End data transformation')

log_progress('Begin data load_csv')

x = load_to_csv(t, csv_path)

log_progress('End data load_csv')

log_progress('Begin data load_db')

y = load_to_db(t, sql_connection, table_name)

log_progress('End data load_db')

log_progress('Begin run_query')

q = run_query(f'SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100',sql_connection)

log_progress('End run_query')

log_progress('End ETL')

sql_connection.close()
