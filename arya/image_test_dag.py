from airflow.decorators import dag, task
from pendulum import datetime
from kubernetes.client import models as k8s

@dag(
    dag_id="arya_custom_image_test",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["arya", "image-test"],
)
def arya_custom_image_test():

    @task(
        executor_config={
            "pod_override": k8s.V1Pod(
                spec=k8s.V1PodSpec(
                    containers=[
                        k8s.V1Container(
                            name="base",
                            image="airflow-arya:1.0.0",
                            image_pull_policy="Never",
                        )
                    ]
                )
            )
        }
    )
    def use_numpy():
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        print(f"Arya image works! numpy sum = {arr.sum()}")
        return int(arr.sum())

    use_numpy()

arya_custom_image_test()
