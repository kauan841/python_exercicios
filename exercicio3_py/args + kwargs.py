def processar(*args,**kwargs):
    total = sum(args)
    print(f'soma : {total}')
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

processar(1, 2, 3, 4, nome="Kauan", idade=16)
    