#import 

from datetime import tiemdelta 
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import bash_operator
# This makes scheduling easy
from airflow.utils.dates import days_ago 

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Ramesh Sannareddy', #the owner name,
    'start_date': days_ago(0), #when this DAG should run from: days_age(0) means today,
    'email': ['ramesh@somemail.com'], #the email address where the alerts are sent to,
    'email_on_failure': True, # whether alert must be sent on failure,
    'email_on_retry': True, # whether alert must be sent on retry,
    'retries': 1, # the number of retries in case of failure, and
    'retry_delay': timedelta(minutes=5), #the time delay between retries.
}


# define the DAG
#here we created a variable named dag by instantiating the DAG class with 
#the following parameters 
dag = DAG(
    dag_id='sample-etl-dag', # the ID of the Dag : this is what we see on the web console
    default_args=default_args, #default_args is a dictionary of all defaults 
    description='Sample ETL DAG using Bash', #helps us in understanding what this DAG does.
    schedule_interval=timedelta(days=1), #tells us how frequently this DAG runs (in this case every day)
)

# define the tasks

# define the first task named extract
extract = BashOperator(
    task_id='extract', #which is a string that helps in identifying the task
    bash_command='echo "extract"', #what bash command it represents
    dag=dag, #which dag this  task belongs to
)

# define the second task named transform
transform = BashOperator(
    task_id='transform',
    bash_command='echo "transform"',
    dag=dag,
)

# define the third task named load

load = BashOperator(
    task_id='load',
    bash_command='echo "load"',
    dag=dag,
)

# define the task pipeline
extract >> transform >> load