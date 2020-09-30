# Dado un cociente de la forma: 3.0/2.2:
#   a) Escribir el valor resultante.
#   b) Escribir el valor resultando únicamente con dos decimales.
#   c) Obtener la parte entera del cociente.
#   d) Convertir el cociente en cadena de caracteres.
#   -------------------------------------------

fNum, fNum2 = 3.0, 2.2

# a) Escribir el valor resultante.
print(fNum/fNum2)

# b) Escribir el valor resultando únicamente con dos decimales.
print(round((fNum/fNum2), 2))

# c) Obtener la parte entera del cociente.
print(fNum//fNum2, round(fNum/fNum2), sep=", ")

# d) Convertir el cociente en cadena de caracteres.
print(str(fNum/fNum2), type(str(fNum/fNum2)), sep=", ")
