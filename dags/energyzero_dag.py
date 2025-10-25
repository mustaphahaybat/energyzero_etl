from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='energyzero_etl',
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract = BashOperator(
        task_id='extract_energyzero_json',
        bash_command='python /opt/airflow/scripts/extract_energyzero.py'
    )

    transform = BashOperator(
        task_id='transform_json_to_parquet',
        bash_command='python /opt/airflow/scripts/transform_pandas.py'
    )

    extract >> transform
