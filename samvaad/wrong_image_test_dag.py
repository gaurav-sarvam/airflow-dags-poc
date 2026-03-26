from airflow.decorators import dag, task
from pendulum import datetime
from kubernetes.client import models as k8s

@dag(
    dag_id="samvaad_wrong_image_test",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["samvaad", "negative-test"],
)
def samvaad_wrong_image_test():

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
    def try_numpy_on_wrong_image():
        import numpy as np  # This should FAIL — numpy not in samvaad image
        print(f"This should never print: {np.array([1]).sum()}")

    try_numpy_on_wrong_image()

samvaad_wrong_image_test()
