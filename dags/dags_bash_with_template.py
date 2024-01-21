

from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator



with DAG(
    dag_id="dags_bash_with_template",
    schedule="0 0 1 * *",
    start_date=pendulum.datetime(2024, 1, 22, tz="Asia/Seoul"),
    catchup=False,

) as dag:
    bash_with_template_t1 = PythonOperator(
        task_id="bash_with_template_t1",
        bash_command='echo "data_interval_end: {{data_interval_end}}"'
    )
    
    bash_with_template_t2= PythonOperator(
        task_id="bash_with_template_t2",
        env={''START_DATE':'{{data_interval_start | ds}}'',
             'END_DATE'|'{{data_interval_end | ds}}'
        },
        bash_command='echo $START_DATE  && echo $END_DATE'
    )
    
    bash_with_template_t1 >> bash_with_template_t2
    