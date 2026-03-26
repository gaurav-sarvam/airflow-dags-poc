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
        print(
            "This Dag line appeared which is made to check changes are picked up or not!!"
        )
        print("TEsting the poc for arya")
        return "magic"

    do_something()


arya_new_feature()
