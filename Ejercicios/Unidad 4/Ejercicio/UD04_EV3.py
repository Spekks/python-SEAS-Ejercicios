#  Ejercicio 3. Unidad 4.
#  ¿Qué hace el siguiente método escrito en Python?

#  El parámetro b debe ser entero positivo para evitar recursión infinita

def misterio(a, b):
    if b == 1:
        return a
    else:
        return a + misterio(a, b-1)


print(misterio(4, 13))
