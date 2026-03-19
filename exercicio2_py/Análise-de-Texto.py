frase = input("Digite uma frase: ")
contagem_letras = {}

for letra in frase:

    if letra != " ":
        contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

print("Resultado:")
for letra, contagem in contagem_letras.items():
    print(f"{letra}: {contagem}")