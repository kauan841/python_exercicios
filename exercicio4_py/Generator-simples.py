def gerador ():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
for numero in gerador():
  
  print(numero)

