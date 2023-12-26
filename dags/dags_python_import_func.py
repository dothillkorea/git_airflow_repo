from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import pythonOperator
from  plugin.common.common_func  import get_sftp


with DAG(
    dag_id="dags_python_common_func",
    schedule="10 6 * * *",
    start_date=pendulum.datetime(2023, 12, 22, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
     
    task_get_sftp=pythonOperator(
        taskid='task_get_sftp',
        python_callable=get_sftp
        
    )
    
   