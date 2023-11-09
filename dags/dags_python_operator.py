
from airflow import DAG
import pendulum
from airflow.operators.python  import PythonOperator
import random




with DAG(
    dag_id="dags_Python_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 11, 9, tz="Asia/Seoul"),
    catchup=False
 
) as dag:
    
    def select_fruit():
        fruit = ['APPLE', 'BANANA', 'ORACLE', 'AVOCADO']
        rand_int = random.randint(0,3)
        print(rand_int)
        
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit
    )
    
    py_t1
    