from opcoes import mostrar_menu, listar_balde, adicionar_balde, apagar_balde

while True:
    mostrar_menu()

    entrada_usuario = input()

    if entrada_usuario == "1":
        print("Você escolheu criar um bucket\n")
        adicionar_balde()

    elif entrada_usuario == "2":
        print("Você escolheu listar os buckets criados\n")
        listar_balde()

    elif entrada_usuario == "3":
        print("Você escolheu apagar um bucket\n")
        apagar_balde()
    
    elif entrada_usuario == "4":
        print("Você escolheu sair do programa. Até mais!")
        break

    else:
        print("Entrada inválida. Por favor, insira uma das opções listadas.")
