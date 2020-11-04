#  Ejercicio 5. Unidad 4. Definir una función a la que se pasa una lista de enteros y devuelve su valor máximo.

lista = [3, 6, 1, 678, 34, 1, 1, 677, 981, 45, 123]


def maximo(lEntero):
    return max(lEntero)


def maximo_manual(lEntero):
    iControl = 0
    for i in lEntero:
        if i > iControl:
            iControl = i
    return iControl


print(maximo(lista))
print(maximo_manual(lista))
