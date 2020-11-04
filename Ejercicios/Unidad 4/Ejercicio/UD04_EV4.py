#  Ejercicio 4. Unidad 4. Escribir un procedimiento sin parámetros que pida un número y escriba la tabla de multiplicar
#  por dicho número. Idem pasando como parámetro el número.

igControl = int(input("Escribe un número entero: "))
igMultiplo = int(input("A multiplicar por: "))


def tabla():
    iControl = int(input("Escribe un número entero: "))
    iMultiplo = int(input("A multiplicar por: "))
    for i in range(1, iMultiplo+1):
        multiplicacion = iControl * i
        print("{} x {} = {}".format(iControl, i, multiplicacion))


def tabla_v2(num, multiplo):
    for i in range(1, multiplo+1):
        multiplicacion = num * i
        print("{} x {} = {}".format(num, i, multiplicacion))


tabla_v2(igControl, igMultiplo)
print(tabla())
