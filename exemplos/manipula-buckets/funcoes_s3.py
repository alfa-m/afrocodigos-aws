from uuid import uuid4
import boto3

cliente_s3 = boto3.client("s3", region_name="us-east-1")

def cria_balde(nome):
    nome_do_bucket = nome + "-" + str(uuid4())

    cliente_s3.create_bucket(Bucket=nome_do_bucket)

    return nome_do_bucket

def lista_balde():
    lista_de_baldes = cliente_s3.list_buckets()

    if len(lista_de_baldes["Buckets"]) > 0:
        print("Lista de buckets atuais:")
        
        for balde in lista_de_baldes["Buckets"]:
            print(f'-> {balde["Name"]}')
    else:
        print("Nenhum bucket no S3")


def deleta_balde(nome):
    cliente_s3.delete_bucket(
        Bucket=nome
    )
    print("Bucket apagado")
    print()
    lista_balde()
