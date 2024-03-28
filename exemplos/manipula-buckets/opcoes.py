from funcoes_s3 import cria_balde, lista_balde, deleta_balde

def mostrar_menu():
    print("="*100)
    print("Digite 1 para criar um bucket")
    print("Digite 2 para listar os buckets criados")
    print("Digite 3 para apagar bucket")
    print("Digite 4 para encerrar o programa")
    print("="*100)

def adicionar_balde():
    nome = input("Digite o nome do bucket: ")

    nome_balde = cria_balde(nome)
    print()
    print(f"Bucket {nome_balde} criado com sucesso!")

def listar_balde():
    lista_balde()

def apagar_balde():
    listar_balde()
    print()
    balde_pra_apagar = input("Por favor, insira o nome do bucket que deseja apagar: ")
    deleta_balde(balde_pra_apagar)
