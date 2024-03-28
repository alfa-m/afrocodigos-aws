import boto3
from pprint import pprint

cliente_ec2 = boto3.client(service_name="ec2",  region_name="us-east-1")

resultado = cliente_ec2.describe_instances()
reservas = resultado['Reservations']
pprint(reservas)
