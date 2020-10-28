#  Ejercicio 1. Unidad 4. Crear una función que determine su un número es perfecto. El número ha de ser introducido por
#  parámetro.

check = False


def perfecto(num):
    divisores = ()
    if num > 0:
        for i in range(num, 0, -1):
            if i != num:
                if num % i == 0:
                    divisores = divisores + (i,)
        if num == sum(divisores):
            print("¡{} es un número perfecto! :)".format(num))
        else:
            print("{} no es un número perfecto :(".format(num))
    else:
        print("{} no puede ser perfecto nunca :(".format(num))


while not check:
    try:
        iNumero = int(input('Escribe un número entero: '))
    except ValueError:
        print("Un número y válido, por favor. :)")
    else:
        check = True

perfecto(iNumero)
