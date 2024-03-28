import boto3
from pprint import pprint

cliente_ec2 = boto3.client(service_name="ec2",  region_name="us-east-1")

# como terminar as instancias
resposta = cliente_ec2.terminate_instances(
    InstanceIds=["i-03e1f5dec701d93f1",
                 "i-0c710d25cc09e19ad",
                 "i-0a392e0a759c606b0"],
)
