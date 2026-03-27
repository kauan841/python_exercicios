lista = []

while True:
    print("\n1 - adicionar item")
    print("2 - listar itens")
    print("3 - sair")
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        item = input("Digite o item: ")
        lista.append(item)
        
    elif opcao == "2":
        print("\nLista de Compras:")
        if not lista:
            print("Lista vazia")
        else:
            for i, item in enumerate(lista):
             print(f"{i + 1} - {item}")

    elif opcao == "3":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")