#  Ejercicio ejecución desde terminal. Unidad 4.

def escribeCuadrado(x):
    print("El cuadrado de {} es {}".format(x, x ** 2))


def escribeCubo(x):
    print("El cubo de {} es {}".format(x, x ** 3))


def escribeCuarta(x):
    print("La cuarta de {} es {}".format(x, x ** 4))


def enterTheNumero():
    try:
        x = int(input("Escribe un número: "))
    except ValueError:
        print("Esa opción no es válida :(")
    else:
        return x


x = enterTheNumero()
comprobar = False

while not comprobar:
    print("Un menú con una serie de opciones.")
    print("1. Escribe el cuadrado de {}".format(x))
    print("2. Escribe el cubo de {}".format(x))
    print("3. Escribe la cuarta potencia de {}".format(x))
    print("4. Salir")

    opcion = enterTheNumero()

    if opcion == 1:
        escribeCuadrado(x)
    elif opcion == 2:
        escribeCubo(x)
    elif opcion == 3:
        escribeCuarta(x)
    elif opcion == 4:
        comprobar = True
    else:
        print("opción no válida :(")
