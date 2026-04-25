lista = [1, 2, 3, 2, 1, 4]

def primeiro_numero_duplicado(lista):
    numeros_vistos = set()
    for numero in lista:
        if numero in numeros_vistos:
            return numero
        numeros_vistos.add(numero)
    return None
resultado = primeiro_numero_duplicado(lista)

print(resultado)