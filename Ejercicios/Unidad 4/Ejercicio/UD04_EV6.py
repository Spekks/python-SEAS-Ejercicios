#  Ejercicio 6. Unidad 4. Definir una función a la que se pasa una lista de enteros y devuelve su valor máximo y mínimo.

lLista = [123, 12, 45, 1, 1, 3, 5, 56, 756, 75, 123, 12, 567, 34]


def maximo_minimo(lEntero):
    iControlMax = max(lEntero)
    iControlMin = min(lEntero)
    return "El valor máximo es {}, mientras que el valor mínimo es {}".format(iControlMax, iControlMin)


def maximo_minimo_manual(lEntero):
    iControlMax = 0
    for i in lEntero:
        if i > iControlMax:
            iControlMax = i
    iControlMin = iControlMax  # Para poder inicializar iControlMin a algo que sea relativo y funcione siempre.
    for i in lEntero:
        if i < iControlMin:
            iControlMin = i
    return "El valor máximo es {}, mientras que el valor mínimo es {}".format(iControlMax, iControlMin)


print(maximo_minimo(lLista))
print(maximo_minimo_manual(lLista))
