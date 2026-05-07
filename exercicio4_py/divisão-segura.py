try:
    primeir_numero = int(input("Digite o primeiro número: "))
    segundo_numero = int(input("Digite o segundo número: "))
    resultado = primeir_numero / segundo_numero
    print(f"O resultado da divisão é: {resultado}")

except ZeroDivisionError as error:
    print(f"Erro: {error}")
    print("Erro: Divisão por zero não é permitida.")

except ValueError as error:
    print(f"Erro: {error}")
    print("Erro: Por favor, digite um número válido.")