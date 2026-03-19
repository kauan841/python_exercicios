estoque = {"Caneta": 50, "Caderno": 20}

while True:
    print("\nMenu:")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Consultar estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ").capitalize()
        qtd = int(input("Quantidade: "))
        estoque[nome] = estoque.get(nome, 0) + qtd
        print("Produto adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do produto: ").capitalize()
        if nome in estoque:
            qtd = int(input("Quantidade a remover: "))
            if estoque[nome] >= qtd:
                estoque[nome] -= qtd
                print("Produto removido com sucesso!")
            else:
                print("Quantidade insuficiente para remover o produto.")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("\nEstoque atual:")
        for produto, qtd in estoque.items():
            print(f"- {produto}: {qtd}")

    elif opcao == "4":
        print("\nEstoque final:")
        for produto, qtd in estoque.items():
            print(f"- {produto}: {qtd}")
        break

    else:
        print("Opção inválida!")