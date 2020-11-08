# Ejercicio guiado 1. Unidad 2

# a) Asignaremos a una variable cad un str. Vamos a acceder a los componentes de la cadena y finalmente vamos a intentar
# cambiar el valor del segundo componente. Dara error al ser inmutable.

cad = "Esto es una cadena de caracteres para el ejercicio guiado de la unidad 2."

print(cad)
print(cad[0:])
print(cad[-1:])
print(cad[7:16])

for i in range(0, len(cad)):
    print(cad[i])

cad[1] = 'b'
print(cad)

# b) Vamos a generar una tupla y vamos a acceder a sus componentes de distintas formas. Finalmente vamos a intentar
# cambiar el valor de un componente para obtener un error.

tTupla = 1, 4, "Antonio", False,

print(tTupla)
print(tTupla[0:])
print(tTupla[:-1])
print(tTupla[2:3])

for i in range(0, len(tTupla)):
    print(tTupla[i])

tTupla[2] = {1: True, 2: False}

# c) Vamos a asignar a una variable lst una lista. Accederemos a sus componentes de distintas formas y vamos a modificar
# su contenido. Vemos que en este caso este puede modificarse. Al igual que e las tuplas, se accede a sus componentes a
# través de corchetes.

lst = [False, 1, 5.9, "False", frozenset([1, 4, 5]), range(1, 3), ["sí", "no"]]

print(lst)

print(lst[0:])
print(lst[4:])
print(lst[:-1])

for i in range(0, len(lst)):
    print(lst[i])

lst[0] = "nanay"
lst.append("illooooooooooooo")
lst.extend([1, 4, ("sí",)])
lst.insert(3, True)

for i in range(0, len(lst)):
    print("Elemento", i, ":", lst[i], "Tipo:", type(lst[i]))

del(lst[5])
lst.pop(2)

for i in range(0, len(lst)):
    print("Elemento", i, ":", lst[i], "Tipo:", type(lst[i]))

# d) Recordando que un diccionario es un par clave-valor, vamos a crear un diccionario, a acceder por sus claves, a
# escribir todas sus claves, a escribir todos sus valores y todo su contenido.

dDic = {"tres": 1, "nueve": "Pepe", "uno": 23+1j, "dos": set({1, 4, False})}

print(dDic)

for clave, valor in dDic.items():
    print(clave, " -> ", valor)

for valor in dDic.values():
    print(valor)

tDic = tuple(dDic.keys())
for i in range(0, len(tDic)):
    print(dDic.get(str(tDic[i])))

for clave in dDic.keys():
    print(clave)

del(dDic["uno"])
print(dDic)

dDic["sexto"] = "Ya ni idea"
print(dDic)

# e) Vamos a utilizar asignación externa para introducir por teclado valores a variables:

sVar = input("Introduce tu nombre: ")
iVar = int(input("Introduce un número entero: "))
fVar = float(input("Introduce un número real: "))

print(sVar, type(sVar), sep=", ")
print(iVar, type(iVar), sep=", ")
print(fVar, type(fVar), sep=", ")
print("Tu nombre es %s, tienes %d años y te faltan %f arbores para madurar" % (sVar, iVar, fVar))
print("Tu nombre es {0}, tienes {1} años y te faltan {2} arbores para madurar".format(sVar, iVar, fVar))

# f) Vamos a crear un conjunto de números enteros y a ver que los números repetidos se eliminan.

sSet = set((1, 1, 3, 4, 5, 5, 7))

print(sSet)
