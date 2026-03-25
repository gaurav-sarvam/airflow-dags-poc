from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    dag_id="arya_new_feature",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["arya", "new"],
)
def arya_new_feature():

    @task
    def do_something():
        print("This DAG appeared without any restart or image rebuild!")
        return "magic"

    do_something()

arya_new_feature()
