cpf = input("Digite o CPF (apenas números): ")
cpf_limpo = cpf.strip().replace(".", "").replace("-", "").replace(" ", "")

# validação básica
if len(cpf_limpo) < 9:
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
        digito_verificador = 0
    else:
        digito_verificador = 11 - resto

    print(f"Primeiro dígito calculado: {digito_verificador}")