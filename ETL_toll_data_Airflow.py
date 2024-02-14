from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'Tolu Babington',
    'start_date': days_ago(0),
    'email': ['tababington@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Simple ETL DAG',
    schedule_interval=timedelta(days=1),
)

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='cd /home/project/airflow/dags/finalassignment; tar -xzf tolldata.tgz',
    dag=dag,)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cd /home/project/airflow/dags/finalassignment; cut -d "," -f1-4 vehicle-data.csv > csv_data.csv',
    dag=dag,)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cd /home/project/airflow/dags/finalassignment; cut -f5- tollplaza-data.tsv | tr '\t' ',' | tr -d '\r'> tsv_data.csv",
    dag=dag,)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="cd /home/project/airflow/dags/finalassignment; rev payment-data.txt|cut -d ' ' -f1-2 | rev | sed 's/ /,/' > fixed_width_data.csv",
    dag=dag,)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="cd /home/project/airflow/dags/finalassignment; paste -d ',' csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv",
    dag=dag,)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command="cd /home/project/airflow/dags/finalassignment; awk -F ',' -v OFS=',' '{$4 = toupper($4)} 1' extracted_data.csv > transformed_data.csv",
    dag=dag,)



unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data