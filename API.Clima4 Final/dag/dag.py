from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from modules.get_data_from_api import DataRetriever
from modules.data_con import DataConn
from modules.alerting import check_alerts
from dotenv import load_dotenv
import os

default_args = {
    'owner': 'nicolas_terradas',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_data_etl',
    default_args=default_args,
    description='ETL DAG for weather data',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

load_dotenv()

def etl():
    config = {
        'REDSHIFT_USERNAME': os.getenv('REDSHIFT_USERNAME'),
        'REDSHIFT_PASSWORD': os.getenv('REDSHIFT_PASSWORD'),
        'REDSHIFT_HOST': os.getenv('REDSHIFT_HOST'),
        'REDSHIFT_PORT': os.getenv('REDSHIFT_PORT'),
        'REDSHIFT_DBNAME': os.getenv('REDSHIFT_DBNAME')
    }
    schema = 'nicolas_terradas_coderhouse'

    data_conn = DataConn(config=config, schema=schema)
    data_conn.get_conn()

    data_retriever = DataRetriever()
    data = data_retriever.get_data()

    table_name = 'weather_data'
    data_conn.upload_data(data, table=table_name)

    data_conn.close_conn()

def alert():
    check_alerts()

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=etl,
    dag=dag,
)

alert_task = PythonOperator(
    task_id='check_alerts',
    python_callable=alert,
    dag=dag,
)

etl_task >> alert_task

