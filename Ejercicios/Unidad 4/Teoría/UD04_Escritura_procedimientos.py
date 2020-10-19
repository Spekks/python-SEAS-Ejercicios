# 1. Escritura de procedimientos:


def hola():  # -> Cabecera
    """ Doctring de la función.
    :return: cad Cadena de caracteres
    """
    cad = input("Saluda ")  # -> Cuerpo
    return cad


print(hola())

# 2. Llamada a procedimientos:


def primero():
    a, b = 1, 2

    def segundo(x, y):
        print(''.join(str(x)), ":", x, ".", ''.join(str(y)), ":", y)

    segundo(a, b)


primero()
