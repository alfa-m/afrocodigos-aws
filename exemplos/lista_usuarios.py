import boto3


clientes = boto3.client("iam")

for user in clientes.list_users()["Users"]:
    print(user["UserName"])
