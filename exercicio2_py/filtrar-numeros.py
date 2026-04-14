def numeros_aleatorios():
    numeros = []

    for i in range(5):
        numero = int(input(f"Digite o número {i + 1}: "))
        numeros.append(numero)
    
    return numeros


def filtrar_maiores_que_10(numeros):
    return [numero for numero in numeros if numero > 10]


def filtrar_menores_que_10(numeros):
    return [numero for numero in numeros if numero < 10]


lista_numeros = numeros_aleatorios()

maiores = filtrar_maiores_que_10(lista_numeros)
menores = filtrar_menores_que_10(lista_numeros)

print(f"Maiores que 10: {maiores}")
print(f"Menores que 10: {menores}")