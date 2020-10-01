# Archivo de pruebas de la unidad 2 - Tipos de datos.

# 1) Tipos de datos que admiten las tuplas:
tTuplaI, tTuplaM = (1, 3, 5, 7), ([1, 3, 4, 5], {"nombre": "Manolo", "edad": 35})

for i in range(0, len(tTuplaI)):
    print("Dato: ", tTuplaI[i], ". Tipo: ", type(tTuplaI[i]))

for i in range(0, len(tTuplaM)):
    print("Dato: ", tTuplaM[i], ". Tipo: ", type(tTuplaM[i]))

# RESUMEN: las tuplas y listas admiten, al contrario que en otros lenguajes, todo tipo de datos.


# 2) ¿Ordenan las tuplas, listas y diccionarios de manera automática sus datos?:
lLista = [1, "Manolo", (True, False), {1: "NO", 2: {"Sí"}}]
dDicc = {"uno": 1, "medio": "hola", "cuatro": {1: "sí", 2: False}}

for i in range(0, len(tTuplaM)):
    print("Número ", i, ": ", tTuplaM[i], " tipo: ", type(tTuplaM[i]))

for i in range(0, len(lLista)):
    print("Número ", i, ": ", lLista[i], " tipo: ", type(lLista[i]))

for clave, valor in dDicc.items():
    print(clave, " -> ", valor)

# RESUMEN: sí, devuelven los datos que contienen por orden de introducción.

# 3) Extraer valores de una lista/tupla y guardarlos en variables:
for i in range(0, len(lLista)):
    if type(lLista[i]) is dict:
        print(lLista[i])
        dDicc = lLista[i]
        print(type(dDicc))
