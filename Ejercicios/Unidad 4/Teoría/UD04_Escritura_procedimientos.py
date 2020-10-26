# 1. Escritura de procedimientos:

'''
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

# 3. Clases de parámetros: inmutables y mutables.

parRealI1, parRealI2, parRealM1, parRealM2 = 34, 2, [3, 4, 56], [2, 3, 5]


def parametro(a):
    a += 1
    print(a)
    return a


def listametros(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] + 1
    print(lst)


def calculos(a, b):
    a -= 1
    b += 2
    print(a, b)


def calculos2(lst):
    lst[0] = 0
    lst[1] = 0
    lst[2] = 0
    print(lst)


print("1: ")
print(parRealI1)
parRealI1 = parametro(parRealI1)
print(parRealI1)

print("2: ")
print(parRealM1)
listametros(parRealM1)
print(parRealM1)

print("3: ")
print(parRealM2)
listametros(parRealM2)
print(parRealM2)

print("4: ")
print(parRealI1)
print(parRealI2)
calculos(parRealI1, parRealI2)
print(parRealI1)
print(parRealI2)

print("5: ")
print(parRealM1)
calculos2(parRealM1)
print(parRealM1)

dicc = {'c1': 10, 'c2': 20, 'c3': 30, 'c4': 40}


def buscar(clave):
    if clave in dicc.values():
        print("La clave existe")
    else:
        print("La clave no existe")


def recorrer(dic):
    for clave in dic:
        print(clave)


buscar(10)
recorrer(dicc)


# 4. Parámetros de nombre:


def frase_random(parr1, parr2="Paco"):
    print("{}, {}".format(parr1, parr2))


frase_random(parr2="Manola", parr1="Adiós")

# 7) Ámbito de los anidamientos.


def persona(nombre, sexo):

    def comer():
        if sexo:
            input("{} no come".format(nombre))
        else:
            input("{} come demasiado".format(nombre))

    comer()


persona("Antonia", True)

# 8. Efectos colaterales.

z1 = 1


def colateral0():
    print(z1)
    z1 = 23


def colateral():
    a, m = 34, 56
    z1 = a / m  # Busca en el ámbito local y crea una variable z1 local, sin llegar a pisar la global.
    return z1


def colateral2():
    global z1
    a, m = 34, 56
    z1 = a / m  # Utiliza directamente la variable z1 global, sin crear una local en la compilación de la función.
    return z1


x1 = z1 + colateral2()  # A partir de aquí la variable global z1 ya ha cambiado su valor a (a/m) y no es 1.
print(x1)

x1 = colateral2() + z1
print(x1)

x1 = z1 + colateral()
print(x1)

x1 = colateral() + z1
print(x1)
'''
# 9. Recursividad.

x = int(input("Escribe un número para ver su factorial: "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(x))
