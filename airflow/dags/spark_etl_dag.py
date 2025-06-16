from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

with DAG(
    dag_id = "spark_etl_job",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup = False
) as dag:

    etl_task = SparkSubmitOperator(
        task_id = "run_spark_etl",
        application="/opt/spark-apps/etl_job.py",
        conn_id = "spark_default",
        verbose = True,
        spark_binary="/opt/bitnami/spark/bin/spark-submit",
        conf={
            "spark.master": "spark://spark-master:7077",
            "spark.hadoop.fs.s3a.access.key": "minioadmin",
            "spark.hadoop.fs.s3a.secret.key": "minioadmin",
            "spark.hadoop.fs.s3a.endpoint": "http://minio:9000",
            "spark.hadoop.fs.s3a.path.style.access": "true",
            "spark.hadoop.fs.s3a.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
        }   
    )