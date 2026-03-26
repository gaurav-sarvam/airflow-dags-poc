from airflow.decorators import dag, task
from pendulum import datetime
from kubernetes.client import models as k8s

@dag(
    dag_id="samvaad_custom_image_test",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["samvaad", "image-test"],
)
def samvaad_custom_image_test():

    @task(
        executor_config={
            "pod_override": k8s.V1Pod(
                spec=k8s.V1PodSpec(
                    containers=[
                        k8s.V1Container(
                            name="base",
                            image="airflow-samvaad:1.0.0",
                            image_pull_policy="Never",
                        )
                    ]
                )
            )
        }
    )
    def use_beautifulsoup():
        from bs4 import BeautifulSoup
        soup = BeautifulSoup("<h1>Samvaad works!</h1>", "html.parser")
        print(f"Samvaad image works! parsed: {soup.h1.string}")
        return soup.h1.string

    use_beautifulsoup()

samvaad_custom_image_test()
