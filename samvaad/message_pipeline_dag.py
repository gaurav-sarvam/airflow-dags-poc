from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    dag_id="samvaad_message_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["samvaad"],
)
def samvaad_message_pipeline():

    @task
    def fetch_messages():
        import time
        print("Samvaad: Fetching messages...")
        time.sleep(3)
        return {"count": 42}

    @task
    def analyze_sentiment(messages):
        print(f"Samvaad: Analyzing {messages['count']} messages...")
        return "positive"

    msgs = fetch_messages()
    analyze_sentiment(msgs)

samvaad_message_pipeline()
