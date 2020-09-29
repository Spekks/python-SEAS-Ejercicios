# Asignar a una variable el cociente 2.0/3.0. Escribir el resultado obtenido, el tipo de variable y redondear con 3
# decimales. Convertir a cadena e imprimir por pantalla

fNum1 = 2.0
fNum2 = 3.0
cociente = fNum1 / fNum2

print(fNum1, "/", fNum2, "es igual a", cociente, sep=" ")
print(type(cociente))
print(round(cociente, 3))

sCociente = str(round(cociente, 3))
print(sCociente, "es de tipo", type(sCociente), sep=" ")
