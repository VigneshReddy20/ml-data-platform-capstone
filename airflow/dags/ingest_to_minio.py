from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def upload_to_minio():
    s3 = S3Hook(aws_conn_id='minio_conn')
    s3.load_file(
        filename = '/opt/airflow/dags/data/iris.csv',
        key = 'raw/iris.csv',
        bucket_name = 'ml-data',
        replace = True
    )