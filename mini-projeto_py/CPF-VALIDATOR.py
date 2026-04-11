cpf = input("Digite o CPF (somente números): ")
cpf_limpo = cpf.strip().replace(".", "").replace("-", "").replace(" ", "")

if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
    print("CPF inválido!")

elif cpf_limpo == cpf_limpo[0] * 11:
    print("CPF inválido!")

else:
    cpf_base = cpf_limpo[:9]

    soma = 0
    peso = 10

    for digito in cpf_base:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    cpf_base2 = cpf_base + str(digito1)

    soma = 0
    peso = 11

    for digito in cpf_base2:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if cpf_limpo == f"{cpf_base}{digito1}{digito2}":
        print("CPF válido!")
    else:
        print("CPF inválido!")