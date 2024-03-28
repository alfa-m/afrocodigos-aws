from uuid import uuid4
import boto3

class Bucket():
    def __init__(self, nome_balde):
        self.nome = nome_balde

class BucketManager():
    def adiciona_balde(self, balde):
        self._balde = balde + "-" + str(uuid4())
        
        cliente_s3 = boto3.client("s3", region_name="us-east-1")
        cliente_s3.create_bucket(Bucket=self._balde)

        return self._balde

    def lista_balde(self):
        cliente_s3 = boto3.client("s3", region_name="us-east-1")
        self._lista_de_baldes = cliente_s3.list_buckets()
        self._tamanho_lista = len(self._lista_de_baldes["Buckets"])

        if self._tamanho_lista > 0:
            print("Lista de buckets atuais:")
        
            for balde in self._lista_de_baldes["Buckets"]:
                print(f'-> {balde["Name"]}')
        else:
            print("Nenhum bucket no S3")
        
    def deleta_balde(self, nome):
        self._nome_balde = nome
        cliente_s3 = boto3.client("s3", region_name="us-east-1")
        cliente_s3.delete_bucket(Bucket=self._nome_balde)
        print("Bucket apagado")
