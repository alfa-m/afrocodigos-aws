from classBalde import Balde, BaldeManager
controle_baldes = BaldeManager()

def mostrar_menu():
    print("="*100)
    print("Digite 1 para criar um bucket")
    print("Digite 2 para listar os buckets")
    print("Digite 3 para apagar bucket")
    print("Digite 4 para encerrar o programa")
    print("="*100)

def listar_balde():
    print("Buckets atuais:")
    controle_baldes.lista_baldes()

def adicionar_balde():
    nome_balde = input("Digite o nome do bucket: ")

    #balde_atual = Balde(nome=nome_balde)
    controle_baldes.adiciona_balde(nome_balde)
    print()
    print(f"Bucket {nome_balde} criado com sucesso!")

def apagar_balde():
    listar_balde()
    balde_pra_apagar = input("Por favor, insira o nome do balde que deseja apagar: ")
    controle_baldes.apaga_balde(balde_pra_apagar)


