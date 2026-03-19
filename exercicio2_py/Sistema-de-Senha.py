senha = input("Digite a senha: ")

tem_numero = any(char.isdigit() for char in senha)
tem_letra = any(char.isalpha() for char in senha)
tem_maiuscula = any(char.isupper() for char in senha)

if len(senha) >= 8 and tem_numero and tem_letra and tem_maiuscula:
    print("Senha válida!")
else:
    print("Senha inválida!")
    print("Regras:")
    print("- Mínimo 8 caracteres")
    print("- Pelo menos 1 número")
    print("- Pelo menos 1 letra")
    print("- Pelo menos 1 letra maiúscula")