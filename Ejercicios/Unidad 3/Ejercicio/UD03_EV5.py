# Escribir el segmento de código para escribir los números pares entre 2 y 100.

MAX_NUMBER = 100
iEntero = 2

for i in range(2, MAX_NUMBER + 1, 2):
    print(i)

while iEntero <= MAX_NUMBER:
    if iEntero % 2 == 0:
        print(iEntero)
    iEntero += 1
