import boto3

cliente_s3 = boto3.client("s3", region_name="us-east-1")

# Deletando um bucket
cliente_s3.delete_bucket(
    Bucket='meu-balde-alfa-marine'
)