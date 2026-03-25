from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    dag_id="arya_audio_processing",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["arya"],
)
def arya_audio_processing():

    @task
    def extract_audio():
        import time
        print("Arya: Extracting audio metadata...")
        time.sleep(5)
        return {"file": "call_001.wav", "duration": 120}

    @task
    def process_audio(metadata):
        print(f"Arya: Processing {metadata['file']}...")
        return "processed"

    data = extract_audio()
    process_audio(data)

arya_audio_processing()
