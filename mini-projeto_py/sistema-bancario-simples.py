conta = {"saldo": 0.0}

def depositar():
    try:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            conta["saldo"] += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O depósito deve ser maior que zero.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido.")

def sacar ():
    try:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > 0:
            if valor <= conta["saldo"]:
                conta["saldo"] -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor inválido. O saque deve ser maior que zero.")
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido.")

def ver_saldo():
    print(f"Saldo atual: R${conta['saldo']:.2f}")



while True:
    print("\nBem-vindo ao Sistema Bancário Simples!")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Saldo")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        depositar()
    elif escolha == "2":
        sacar()
    elif escolha == "3":
        ver_saldo()
    elif escolha == "4":
        print("Obrigado por usar o Sistema Bancário Simples. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")