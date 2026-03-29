frase = input("Digite uma frase: ")
palavras = frase.split()
frase_junta = "-".join(palavras)

print("Frase original:", frase)
print("Frase com palavras separadas por - :", frase_junta)