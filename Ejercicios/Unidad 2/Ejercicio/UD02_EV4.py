# Escribir una lista lv vacía y otra l5 de 5 números reales nulos. Escribir las listas. Utilizar la función range()
# para escribir:
#   - Los enteros de índice 0 a 2.
#   - Los enteros de índice de 3 a 6.
#   - Los enteros de índice 1 a 5 con pasos de 2 en 2.
#   --------------------------------------------------

lv = []
print(lv)

l5 = [0.0 for i in range(1, 6)]
print(l5)

#   - Los enteros de índice 0 a 2.
lv = [i for i in range(1, 4)]
print("a):", lv, sep=" ")

#   - Los enteros de índice de 3 a 6.
lv = [i for i in range(4, 8)]
print("b):", lv, sep=" ")

#   - Los enteros de índice 1 a 5 con pasos de 2 en 2.
lv = [i for i in range(2, 11, 2)]
print("c):", lv, sep=" ")

"""
lWords = [chr(i) for i in range(65, 91)]
print(lWords, "; tipo: ", type(lWords))
"""