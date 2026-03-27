
while True:
    print("\nvocê quer digitar os nomes ou sair?")
    opcao = input("Digite 'nomes' para digitar os nomes ou 'sair' para sair: ")
    
    if opcao == "nomes":
        nomes = input("Digite três nomes separados por espaço: ")
        if len(nomes.split()) != 3:
            print("Por favor, digite exatamente três nomes.")
            continue
        for i, nome in enumerate(nomes.split()):
            print(f"{i + 1} - {nome}")
    
    elif opcao == "sair":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")