from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator


@dag(
        dag_id="operators_dag",
)
def operators_dag():

    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")

    @task.bash
    def modern_bash_task():
        return "echo https://airflow.apache.org/"

    traditional_bash_operator = BashOperator(
    task_id="traditional_bash_operator",
    bash_command="echo https://airflow.apache.org/",
    )


    # defining task dependencies
    first = first_task()
    second = second_task()
    bash_modern = modern_bash_task()
    bash_traditional = traditional_bash_operator

    first >> second >> bash_modern >> bash_traditional


# Instantiating the DAG
operators_dag()