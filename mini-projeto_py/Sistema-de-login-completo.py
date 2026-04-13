cadastro = []

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for usuario in cadastro:
        if usuario["email"] == email:
            print("❌ Email já cadastrado.")
            return

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    cadastro.append(usuario)
    print("✅ Usuário cadastrado com sucesso!")


def login():
    print("\n=== Login ===")
    tentativas = 3

    while tentativas > 0:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        for usuario in cadastro:
            if usuario["email"] == email and usuario["senha"] == senha:
                print(f"✅ Bem-vindo, {usuario['nome']}!")
                menu_logado(usuario)
                return

        tentativas -= 1
        print(f"❌ Email ou senha incorretos. Tentativas restantes: {tentativas}")

    print("🚫 Muitas tentativas. Acesso bloqueado.")


def menu_logado(usuario):
    while True:
        print(f"\n=== Logado como {usuario['nome']} ===")
        print("1. Ver meus dados")
        print("2. Logout")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("\n--- Seus dados ---")
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
        elif opcao == "2":
            print("👋 Logout realizado.")
            break
        else:
            print("❌ Opção inválida.")


def main():
    while True:
        print("\n=== Sistema de Login ===")
        print("1. Cadastrar Usuário")
        print("2. Login")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            login()
        elif escolha == "3":
            print("👋 Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()