from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator

dag = DAG('Ejercicio_Final', description='Ejercicio Final del Track Basico',
          schedule_interval='* * * * *',
          start_date=datetime(2022, 5, 31), catchup=False)

run_playbook = BashOperator(
    task_id='bash_get_path',
    bash_command='ansible-playbook /home/santilopez/Documents/GitHub/Sprint0/Track_Basico_Ejercicio_Final/playbook_metricas_pc.yml',
    dag=dag
)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)
dummy_operator >> run_playbook
