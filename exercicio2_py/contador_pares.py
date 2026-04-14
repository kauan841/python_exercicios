def contar_pares(*args):
    quantidade_pares = 0
    for numero in args:
        if numero % 2 == 0:
            quantidade_pares += 1
    return quantidade_pares


resultado = contar_pares(1, 2, 3, 4, 5, 6)
print(resultado)