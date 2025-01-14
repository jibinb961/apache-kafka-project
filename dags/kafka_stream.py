from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2025,1,14,10,00)
}

def stream_data():
    import json
    import requests

    res= requests.get('https://randomuser.me/api/')
    res = res.json()
    res = res['results'][0] # just to make sure that we take the first entry from the results json, even though we just have one result.
    print(json.dumps(res,indent=3))


# with DAG('user_automation',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
#     streaming_task= PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()