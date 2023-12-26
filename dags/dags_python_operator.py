from airflow import DAG
import pendulum , random
import datetime
from airflow.operators.python import pythonOperator


with DAG(
    dag_id="dags_python_operator",
    schedule="10 6 * * *",
    start_date=pendulum.datetime(2023, 12, 18, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    def select_fruit():
        fruit=['APPLE','BANANA','ORANGE', 'FINEAPPLE']
        rand_int=random.randint(0,3)
        print(fruit[rand_int])
    
    py_t1=pythonOperator(
        taskid='py_t1',
        python_callable=select_fruit
        
    )
    
    py_t1