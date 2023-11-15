import os
import boto3
from dotenv import load_dotenv


load_dotenv()


minio_endpoint = os.environ.get('MLFLOW_S3_ENDPOINT_URL')
access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
bucket_name = os.environ.get('MLFLOW_BUCKET_NAME')


def create_minio_bucket():
    s3 = boto3.client('s3',
                    endpoint_url=minio_endpoint,
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key)
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    create_minio_bucket()


