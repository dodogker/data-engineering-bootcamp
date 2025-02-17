from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id      = "my_first_dag",
    schedule    = "0 17 1,16 * *",
    start_date  = timezone.datetime(2023, 8, 27),
    catchup     = False,
    tags        = ["DEB", "2023"],

):
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")
    t3 = EmptyOperator(task_id="t3")
    t4 = EmptyOperator(task_id="t4")
    t5 = EmptyOperator(task_id="t5")
    t6 = EmptyOperator(task_id="t6")
    t7 = EmptyOperator(task_id="t7")
    t8 = EmptyOperator(task_id="t8")
    t9 = EmptyOperator(task_id="t9")

    t1 >> t2 >> t3 >> t4 >> t9
    t2 >> t6 >> t8
    t1 >> t5 >> t6
    t1 >> t5 >> t7 >> t8 >> t9