while True:
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    idade = int(input("Digite sua idade: "))
    
    status_valido = True

    if not nome.strip():
        print(f"Nome: {nome} não pode estar vazio!")
        status_valido = False

    if "@" not in email:
        print(f"Email: {email} deve conter '@'!")
        status_valido = False

    if len(senha) < 6:
        print(f"Senha inválida! Mínimo 6 caracteres.")
        status_valido = False

    if idade < 13:
        print(f"Idade mínima é 13 anos.")
        status_valido = False

    if status_valido:
        print("Cadastro realizado com sucesso!")
        print(f"Nome: {nome} | Email: {email} | Idade: {idade}")
        break
    else:
        print("Algum dado está inválido. Tente novamente.\n")