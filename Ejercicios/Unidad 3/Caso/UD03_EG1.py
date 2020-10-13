# Ejercicio guiado 1. Unidad 3

# a) Escribir algo parecido a un menú para elegir una entre varias opciones. Última línea muestra el resultado:

letter = input("Escriba la letra 'a', 'b' o 'c': ")

if letter == 'a':
    print("Opción a")
elif letter == 'b':
    print("Opción b")
elif letter == 'c':
    print("Opción c")
else:
    print("No has seleccionado una de las opciones válidas.")

# b) Vamos a introducir un conjunto de números enteros que van a ser elementos de un conjunto, de forma que
# automáticamente se eliminen los repetidos. Tras eso, el conjunto se va a convertir en una lista en la que no haya
# elementos repetidos.

num = set()

print("Introduce 5 números:")
for i in range(5):
    num.add(int(input()))

lNum = list(num)

print(lNum, type(lNum), sep=", ")

# c) Vamos a introducir por teclado los elementos de una lista y vamos a crear otra con dichos elementos que quede
# ordenada de mayor a menor. Para ello se obtendrá el mayor, se introducirá en una lista y se eliminará de la primera.
# Así se hará hasta tener todos los componentes en la segunda lista. A continuación, se escribirán en pantalla con los
# símbolos > o = adecuados en cada caso.

n, lst1, lst2, sep, lst3 = None, [], [], [], []

n = int(input("Cuántos números quieres introducir? "))
print("Números: ")
for i in range(n):
    lst1.append(int(input()))

print("Lista 1:", lst1, "lista 2:", lst2)

for i in range(n):
    c = max(lst1)
    lst1.remove(c)
    lst2.append(c)

print("lista 1:", lst1, "lista 2:", lst2)

for i in range(n-1):
    if lst2[i] != lst2[i+1]:
        sep.append(">")
    else:
        sep.append("=")

print(sep)

for i in range(n):
    if i < n-1:
        lst3.extend([lst2[i], sep[i]])
    else:
        lst3.append(lst2[i])

print(lst3)
print("lista ordenada: ", ' '.join(str(i) for i in lst3))

