#  Ejercicio guiado. Unidad 4.

#  a) Vamos a dibujar cuadrados rellenos utilizando el carácter car que se pasará como argumento. Se pasan también el
#  desplazamiento de cada línea (valor de a) y el número de caracteres que se escriben (valor de b) que es igual al
#  número de líneas que se escriben. Todos ellos son de entrada (pasados por valor).

comprobar = False
while not comprobar:
    caracter = input("Escribe un carácter: ")
    if len(caracter) > 1:
        print("inténtalo otra vez.")
    else:
        comprobar = True

x = int(input("Escribe un número:"))
y = int(input("Escribe un número:"))


def cuadrado(a, b, car):
    #  Lo que pide el ejercicio
    for i in range(b):
        print(" " * a, (car + " ") * b)


def cuadrado2(a, b, car):
    #  Lo que para mí tendría sentido
    for i in range(a):
        print((car + " ") * b)


cuadrado(x, y, caracter)
cuadrado2(x, y, caracter)

#  b) En este ejercicio se utiliza en la izquierda una variable local s cuyo valor se quiere imprimir antes de haberle
#  asignado un valor. Genera un error.


def f():
    global s  # Si no asignamos la variable s como global, que traeremos luego en ámbito global, no funciona.
    print(s)
    s = "Hola, ¿quién eres?"  # Al haber definido s como global, esta instancia de s NO es local, es la variable global.
    print(s)


s = "Hola, soy Pepe"
f()
print(s)  # Imprimirá el nuevo valor de s instanciado dentro de la función f(), pues esta utiliza s global.

#  c) Vamos a usar parámetros mutables para ver el efecto del procedimiento sobre estos parámetros. Para ello, vamos a
#  pasar una lista de enteros a la función y vamos a hacer que devuelva la lista ordenada. Lo hacemos como ejercicio, ya
#  que en la práctica existe un método (sort) que realiza esta operación.

lNumeros = [30, 1, 43, 2, 45, 1, 4, 4, 13]


def ordenar(lst):
    for z in range(len(lst)-1):
        iControl = lst[z]
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                iControl = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = iControl
    print(lst)


ordenar(lNumeros)
