from uuid import uuid4
import boto3

cliente_s3 = boto3.client("s3", region_name="us-east-1")

def cria_balde(nome):
    nome_do_bucket = nome + "-" + str(uuid4())

    cliente_s3.create_bucket(
    Bucket=nome_do_bucket, CreateBucketConfiguration={"LocationConstraint": "us-east-2"}
    )

def lista_balde():
    lista_de_baldes = cliente_s3.list_buckets()
    return lista_de_baldes

def deleta_balde(nome):
    cliente_s3.delete_bucket(
        Bucket=nome
    )