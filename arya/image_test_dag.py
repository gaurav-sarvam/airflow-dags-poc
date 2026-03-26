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
                            image="airflow-arya:1.0.1",
                            image_pull_policy="Never",
                        )
                    ]
                )
            )
        }
    )
    def use_librosa():
        import librosa
        print(f"Arya image works! librosa version = {librosa.__version__}")
        return "success"

    use_librosa()

arya_custom_image_test()
