def filtrar_e_transformar(numeros):
    return [numero * 2 for numero in numeros if numero > 20 ]

numeros = [10, 15, 20, 25, 30, 35, 40]
resultado = filtrar_e_transformar(numeros)
print(resultado)