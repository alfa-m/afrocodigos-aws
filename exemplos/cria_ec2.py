import boto3
from pprint import pprint

cliente_ec2 = boto3.client(service_name="ec2",  region_name="us-east-1")

resposta = cliente_ec2.run_instances(
    ImageId="ami-0c101f26f147fa7fd",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1
    )
pprint(resposta)
