#  Ejercicio 2. Unidad 4. Utilizar el script del Ejercicio 1 para determinar y escribir los cuatro primeros números
#  perfectos.

def perfecto(num):
    divisores = ()
    if num > 0:
        for i in range(num, 0, -1):
            if i != num:
                if num % i == 0:
                    divisores = divisores + (i,)
        if num == sum(divisores):
            return num


def calcular():
    lPerfectos, iContador, iTemp = [], 1, None
    while len(lPerfectos) <= 3:
        iTemp = perfecto(iContador)
        if iTemp is not None:
            lPerfectos.append(perfecto(iTemp))
        iContador += 1
    print(lPerfectos)


calcular()
