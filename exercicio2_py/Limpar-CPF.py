cpf = input("Digite um CPF: ")
cpf_limpo = cpf.strip().replace(".", "").replace("-", "").replace(" ", "")

print(cpf_limpo)