# Escribir un programa que asigne a una variable el radio de una circunferencia y escriba en pantalla la longitud de su
# circunferencia y el área del círculo.

import math

# Variables:
r = float(input("Escriba el radio: "))  # La función input() crea un string, hay que hacer conversión explícita a float.

# Longitud de la circunferencia:
long = 2 * math.pi * r

# Área del círculo:
a1 = math.pi * r ** 2
a2 = math.pi * pow(r, 2)

# Salida por pantalla:
print("El radio vale ", r)
print("===========")
print("Longitud de la circunferencia: ", long)
print("El área del círculo vale: ", a1, " / ", a2)



