from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from modules.validate_credentials import validate_credentials
from modules.extract_data import extract_data
from modules.data_transformation import transform_data
from modules.clean_and_transformation import clean_data
from modules.anonymize_column import anonymize_column
from modules.load_data import load_data
from parameters import API_URL
from dotenv import load_dotenv

load_dotenv()

def validate_credentials():
    if not validate_credentials():
        raise ValueError("Invalid credentials. Exiting...")
    
def extract_and_transform_data(**kwargs):
    data = extract_data(API_URL)
    if data:
        transformed_data = transform_data(data)
        cleaned_data = clean_data(transformed_data)
        kwargs['ti'].xcom_push(key='cleaned_data', value=cleaned_data)
    else:
        raise ValueError("No data extracted.")

def transform_and_anonymize_data(**kwargs):
    ti = kwargs['ti']
    cleaned_data = ti.xcom_pull(task_ids='extract_and_transform_data', key='cleaned_data')
    anonymized_data = anonymize_column(cleaned_data)
    ti.xcom_push(key='anonymized_data', value=anonymized_data)

def load_data_task(**kwargs):
    ti = kwargs['ti']
    anonymized_data = ti.xcom_pull(task_ids='transform_and_anonymize_data', key='anonymized_data')
    load_data(anonymized_data)

default_args = {
    'owner': 'juan_ml',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'exchange_rate_dag',
    default_args=default_args,
    description='DAG para extraer, transformar y cargar datos de tasas de cambio',
    schedule_interval=timedelta(days=1),
)

with dag:
    task_extract_and_transform = PythonOperator(
        task_id='extract_and_transform_data',
        python_callable=extract_and_transform_data,
        provide_context=True
    )

    task_anonymize = PythonOperator(
        task_id='transform_and_anonymize_data',
        python_callable=transform_and_anonymize_data,
        provide_context=True
    )

    task_load = PythonOperator(
        task_id='load_data',
        python_callable=load_data_task,
        provide_context=True
    )

    task_extract_and_transform >> task_anonymize >> task_load
