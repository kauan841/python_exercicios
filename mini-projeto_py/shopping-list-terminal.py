lista = []

while True:
    print("\n1 - adicionar item")
    print("2 - listar itens")
    print("3 - remover item")
    print("4 - marcar item como comprado")
    print("0 - sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item: ")
        lista.append({"item": item, "comprado": False})


    elif opcao == "2":
        print("\nLista de Compras:")
        if not lista:
            print("Lista vazia")
        else:
            for i, produto in enumerate(lista):
                status = "x" if produto["comprado"] else " "
                print(f"{i + 1} - {produto['item']} [{status}]")


    elif opcao == "3":
        print("\nRemover Item:")
        for i, produto in enumerate(lista):
            print(f"{i + 1} - {produto['item']}")

        indice = int(input("Digite o número do item: "))

        lista.pop(indice - 1)
        print("Item removido com sucesso!")


    elif opcao == "4":
        print("\nMarcar Item como Comprado:")

        for i, produto in enumerate(lista):
            print(f"{i + 1} - {produto['item']}")
            
        indice = int(input("Digite o número do item: "))
        lista[indice - 1]["comprado"] = True
        print("Item marcado como comprado!")


    elif opcao == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
    
  