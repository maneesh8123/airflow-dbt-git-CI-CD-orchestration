# airflow-dbt-git-CI-CD-orchestration

### Running Ariflow in Docker
[Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html?utm_source=chatgpt.com#running-airflow-in-docker)
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.5/docker-compose.yaml'

docker compose up -d --build - build the image

##### Create an .env file 
AIRFLOW_IMAGE_NAME=apache/airflow:3.1.5
AIRFLOW_UID=50000


_AIRFLOW_WWW_USER_USERNAME= airflow
_AIRFLOW_WWW_USER_PASSWORD= airflow

# dbt Databricks Token
DBT_DATABRICKS_TOKEN= your token
