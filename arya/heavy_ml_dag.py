from airflow.decorators import dag, task
from pendulum import datetime
from kubernetes.client import models as k8s

@dag(
    dag_id="arya_heavy_ml_task",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["arya", "heavy"],
)
def arya_heavy_ml_task():

    @task(
        executor_config={
            "pod_override": k8s.V1Pod(
                spec=k8s.V1PodSpec(
                    tolerations=[
                        k8s.V1Toleration(
                            key="workload",
                            value="heavy",
                            effect="NoSchedule"
                        )
                    ],
                    node_selector={"nodepool": "high-memory"},
                    containers=[
                        k8s.V1Container(
                            name="base",
                            resources=k8s.V1ResourceRequirements(
                                requests={"memory": "256Mi", "cpu": "250m"},
                                limits={"memory": "512Mi", "cpu": "500m"}
                            )
                        )
                    ]
                )
            )
        }
    )
    def train_model():
        import time
        print("Arya: Training ML model on high-memory node...")
        time.sleep(10)
        return {"accuracy": 0.95}

    @task
    def save_results(metrics):
        print(f"Arya: Model accuracy = {metrics['accuracy']}")

    metrics = train_model()
    save_results(metrics)

arya_heavy_ml_task()
