# Definir la lista: lista = [16, 28, 5, 37, 22, 33] y opera:

lista = [16, 28, 5, 37, 22, 33]

# a) Calcular su longitud, es decir el número de elementos, y escribir la lista.
print("Longitud:", len(lista), sep=" ")
print("Lista:", lista, sep=" ")

# b) Escribir el tipo de variable.
print("Tipo:", type(lista), sep=" ")

# c) Añadir a la lista el número 30 y escribir la lista resultante. Trabaja con esta lista en adelante.
lista.append(30)
print("Lista:", lista, sep=" ")

# d) Ordenar la lista y escribirla.
lista.sort()
print("Lista orden +:", lista, sep=" ")

# e) Invertirla y escribirla.
lista.reverse()
print("Lista orden -:", lista, sep=" ")

# f) Calcular el índice correspondiente al número 28.
print("Índex 28:", lista.index(28), sep=" ")

# g) Escribir la lista del índice 3 al 5.
print("Lista del 3 al 5:", lista[2:5], sep=" ")

# h) Escribir la lista que va del primer componente al tercero.
print("Lista del 0 al 3:", lista[:3], sep=" ")

# i) Escribir la lista que va del cuarto componente al último.
print("Lista del 3 al último:", lista[3:], sep=" ")

# j) Utilizando índices negativos, escribir los dos últimos componentes.
print("Lista del último al penúltimo:", lista[-2:], sep=" ")
