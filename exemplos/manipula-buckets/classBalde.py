from pprint import pprint
from funcoes_s3 import cria_balde, lista_balde, deleta_balde
import boto3

cliente_s3 = boto3.client("s3", region_name="us-east-1")

class Balde():
    def __init__(self, nome):
        self.nome = nome

class BaldeManager():
    _lista_baldes = []

    def adiciona_balde(self, balde):
        self.nome = balde
        cria_balde(self.nome)

    def lista_baldes(self):
        self.resposta = lista_balde()
        self._lista_baldes = self.resposta["Buckets"]
        print("Listando buckets:")
        
        for balde in self._lista_baldes:
            pprint(f'  {balde["Name"]}')

    def apaga_balde(self, balde):
        deleta_balde(balde)
