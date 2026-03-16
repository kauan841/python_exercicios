nome = input("Digite seu nome: ")

try:
  idade = int(input("Digite sua idade: "))
  salario = int(input("Digite seu salário: "))
  
  print("Funcionário cadastrado:")
  print(f"nome : {nome}")
  print(f"idade : {idade}")
  print(f"salário : {salario}")

except ValueError:
  print("Erro: valor inválido. Digite apenas números.")