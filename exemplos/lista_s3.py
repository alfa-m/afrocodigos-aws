from pprint import pprint
import boto3

cliente_s3 = boto3.client("s3", region_name="us-east-1")
resposta = cliente_s3.list_buckets()

# Listando os buckets existentes
print("Listando buckets:")
for balde in resposta["Buckets"]:
    pprint(f'  {balde["Name"]}')
