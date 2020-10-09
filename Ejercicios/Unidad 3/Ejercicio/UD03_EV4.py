# Escribir el código para escribir los enteros impares entre 1 y 19.

iEntero = int(input("Escribe un número impar: "))

if iEntero % 2 != 0:
    for iEntero in range(iEntero, 0, -1):
        if iEntero % 2 != 0:
            print(iEntero)
else:
    print("No has introducido un número impar, subnormal")

if iEntero % 2 != 0:
    for iEntero in range(iEntero, 0, -2):
        print(iEntero)
else:
    print("No has introducido un número entero, subnormal*2")

MAX_NUMBER = 19

for i in range(1, MAX_NUMBER + 2, 2):
    print(i)
