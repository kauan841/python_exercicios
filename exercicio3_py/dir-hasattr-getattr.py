string = 'kauan'
metedo = 'upper1'

if hasattr(string, metedo):
    print(f"O método '{metedo}' existe na string.") 
    funcao = getattr(string, metedo)
    resultado = funcao()
    print(resultado)
else:
    print(f"O método '{metedo}' não existe na string.")