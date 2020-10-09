# Escribir un programa para el cálculo de los 20 primeros número de la sucesión de Fibonacci.
# Con bucle FOR:
x, y, iControl = 1, 0, 0

for i in range(1, 21):
    print(i, ": ", x)
    y = x
    x = iControl + y
    iControl = y

# Con bucle WHILE:
x, y, iControl, i = 1, 0, 0, 1

while i <= 20:
    print(i, ": ", x)
    y = x
    x = iControl + y
    iControl = y
    i += 1

# Con entrada por parámetros:
x, y, iControl = 1, 0, 0
i = int(input("¿Hasta cuándo quiere Fibonacci? "))

for i in range(1, i+1):
    print(i, ": ", x)
    y = x
    x = iControl + y
    iControl = y
