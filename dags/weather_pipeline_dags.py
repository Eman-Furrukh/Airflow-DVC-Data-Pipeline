from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def collect_data():
    os.system("python main.py")  # Script you used to collect weather data

def preprocess_data():
    os.system("python process_data.py")

default_args = {
    'start_date': datetime(2025, 5, 1),
    'retries': 1,
}

with DAG('weather_data_pipeline',
         default_args=default_args,
         schedule_interval='@daily',  # or manually trigger
         catchup=False) as dag:

    collect_task = PythonOperator(
        task_id='collect_weather_data',
        python_callable=collect_data
    )

    preprocess_task = PythonOperator(
        task_id='preprocess_weather_data',
        python_callable=preprocess_data
    )

    collect_task >> preprocess_task
