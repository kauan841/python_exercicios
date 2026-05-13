import conta

print("Resultado da soma: ", conta.soma(5, 3))
print("Resultado da multiplicação: ", conta.multiplicar(5, 3))



from conta import soma, multiplicar
print("Resultado da soma: ", soma(9, 3))
print("Resultado da multiplicação: ", multiplicar(3, 3))

from conta import soma as sm, multiplicar as mt
print("Resultado da soma: ", sm(4, 3))
print("Resultado da multiplicação: ", mt(5, 3))