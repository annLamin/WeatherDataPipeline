from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from openweather_etl import run_openweather_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': 'airflow@example.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'start_date': datetime(2022, 7, 1),
}

dag = DAG(
    'openweather_dag',
    deafult_args = default_args,
    description = 'My first Airflow project'
        )

run_etl = PythonOperator(
    task_id = 'Complete_openweather_etl',
    python_callable = run_openweather_etl,
    dag = dag
)