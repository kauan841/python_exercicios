usuario = input("Usuário válido: ")
senha = input("Digite a senha: ")


if usuario == "admin" and senha == "1234":
     print("Acesso liberado com sucesso.")
else:
     print("Usuário ou senha incorretos.")