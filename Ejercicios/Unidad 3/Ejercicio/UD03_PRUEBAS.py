# Fichero de pruebas para la Unidad 3: estructuras de control.

# Variables:
x, y, z, a, b = 0, False, 3, 6, 4

'''
# Funciones:
def mayor100(i_num):
    """Función que recibe un parámetro y comprueba si es par o no."""
    if i_num % 2 == 0:
        print("par")
    else:
        print("impar")


# Código:
"""Sentencia condicional IF/ELIF/ELSE simple con 2 variables."""
if x > y:
    print(x, "es mayor que", y)
elif y > x:
    print(y, "es mayor que", x)
else:
    print("Ni", x, "ni", y, "son mayores uno que otro.")

"""Sentencia condicional IF/ELSE con una variable y una función dentro."""
if x > 0:
    print(x, "es mayor que 0")
    mayor100(x)
else:
    print(x, "es menor que 0")
    mayor100(x)

"""Sentencia iterativa WHILE"""
while not y:
    print("hola")
    x += 1
    if x == 10:
        y = True
'''
while z < 10:
    z += 1
    print(z, z**2, z**3)
