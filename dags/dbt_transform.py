from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
    # 'email': ['maneesh33a@gmail.com'],
    # 'email_on_failure': True,
    # 'email_on_retry': False,
}
with DAG(
    'dbt_databricks_workflow',
    default_args=default_args,
    description='A DAG to clone dbt repo and run dbt commands on Databricks',
    schedule=None,
    catchup=False,
) as dag:
    repo_url = "https://github.com/maneesh8123/DBT-Data-Build-Tool-with-CI-CD-Databricks.git"
    dbt_project_dir = "/tmp/dbt_project/dbtelt"

    clone_repo = BashOperator(
        task_id='clone_repo',
        bash_command=f'rm -rf /tmp/dbt_project && git clone {repo_url} /tmp/dbt_project',
    )

    dbt_debug = BashOperator(
        task_id='dbt_debug',
        bash_command=f'cd {dbt_project_dir} && dbt debug --profiles-dir /opt/airflow/config',
    )

    dbt_build_dev = BashOperator(
        task_id='dbt_build_dev',
        bash_command=f'cd {dbt_project_dir} && dbt build --target dev --profiles-dir /opt/airflow/config',
    )
    dbt_build_prod = BashOperator(
        task_id='dbt_build_prod',
        bash_command=f'cd {dbt_project_dir} && dbt build --target prod --profiles-dir /opt/airflow/config',
    )

    
    clone_repo >> dbt_debug >> dbt_build_dev >> dbt_build_prod