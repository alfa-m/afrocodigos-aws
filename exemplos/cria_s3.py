# from uuid import uuid4
import boto3

cliente_s3 = boto3.client("s3", region_name="us-east-1")

#nome_do_bucket = "meu-balde-alfa-marine-" + str(uuid4())
nome_do_bucket = "meu-baldinho-alfa-marine"

# Criando um bucket
cliente_s3.create_bucket(
    Bucket=nome_do_bucket, CreateBucketConfiguration={"LocationConstraint": "us-east-2"}
)
