from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from modules.data_con import DataConn
from modules.get_data_from_api import DataRetriever
import os
from dotenv import load_dotenv

load_dotenv()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_etl',
    default_args=default_args,
    description='ETL process for weather data',
    schedule_interval=timedelta(days=1),
)

def extract_data():
    data_retriever = DataRetriever(city="London")
    data = data_retriever.get_data()
    return data

def load_data(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='extract_data')
    config = {
        'REDSHIFT_USERNAME': os.getenv('REDSHIFT_USERNAME'),
        'REDSHIFT_PASSWORD': os.getenv('REDSHIFT_PASSWORD'),
        'REDSHIFT_HOST': os.getenv('REDSHIFT_HOST'),
        'REDSHIFT_PORT': os.getenv('REDSHIFT_PORT'),
        'REDSHIFT_DBNAME': os.getenv('REDSHIFT_DBNAME')
    }
    data_conn = DataConn(config=config, schema='my_schema')
    data_conn.upload_data(data, table='weather_data')

extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    provide_context=True,
    dag=dag,
)

extract_data_task >> load_data_task