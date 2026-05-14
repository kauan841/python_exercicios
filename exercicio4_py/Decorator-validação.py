def validar_entrada(func):

    def wrapper(*args, **kwargs):

        if not args or not all(isinstance(x, (int, float)) for x in args):
            raise TypeError("Todos os argumentos devem ser números.")

        return func(*args, **kwargs)

    return wrapper


@validar_entrada
def somar(a, b):
    return a + b


try:
    print(somar(5, 10))
    print(somar(5, "10"))

except TypeError as error:
    print(f"Erro: {error}")