from classBalde import Bucket, BucketManager

gerente_balde = BucketManager()

def mostrar_menu():
    print("="*100)
    print("Digite 1 para criar um bucket")
    print("Digite 2 para listar os buckets criados")
    print("Digite 3 para apagar bucket")
    print("Digite 4 para encerrar o programa")
    print("="*100)

def adicionar_balde():
    nome = input("Digite o nome do bucket: ")

    balde = Bucket(nome_balde=nome)
    nome_balde = gerente_balde.adiciona_balde(balde.nome)
    print()
    print(f"Bucket {nome_balde} criado com sucesso!")

def listar_balde():
    gerente_balde.lista_balde()

def apagar_balde():
    gerente_balde.lista_balde()
    print()
    balde_pra_apagar = input("Por favor, insira o nome do bucket que deseja apagar: ")
    gerente_balde.deleta_balde(balde_pra_apagar)
