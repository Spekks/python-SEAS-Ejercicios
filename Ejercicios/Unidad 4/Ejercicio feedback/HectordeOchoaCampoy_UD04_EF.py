#  Programa que contiene un menú que gestiona los empleados de una empresa introducidos en un diccionario. El menú
#  consta de 6 opciones, no adimtiéndose ninguna más y terminando su ejecución al pulsar la opción 6.
#  Los valores introducidos deben comprobarse antes de su introducción.

import re
from datetime import datetime, date

#  Variables:

"""Diccionario que contendrá el listado de cliente"""
listadoClientes = {}


def comprobarDni():
    """
    Función que comprueba que el DNI introducido por teclado coincida con el formato que se establece en la variable
    patronD. Mientras que no coincida, se repetirá el bucle y no saldrá.
    :return: string con un DNI.
    """
    comprobar = False
    patronD = re.compile(r'^\d{8}-[A-Z]$')  # Debe contener 8 dígitos, un guion (-) y una letra mayúscula.
    while not comprobar:
        dni = str(input("Introduzca un DNI: "))
        if patronD.match(dni):
            comprobar = True
        else:
            print("--- Formato de DNI no válido.")
    return dni


def comprobarNombreApellidos():
    """
    Función que comprueba que el nombre y apellidos introducidos por teclado coincidan con el formato que se establece
     en la variable patronN. Mientras que no coincida, se repetirá el bucle y no saldrá.
    :return: string con un nombre y apellidos.
    """
    comprobar = False
    patronN = re.compile(r'^([A-Z][a-z]+[\s]*){2,4}$')  # Debe repetirse una letra mayúscula y letras minúsculas 2 o 3
                                                        # veces.
    while not comprobar:
        nombre = str(input("Introduzca nombre y apellidos: "))
        if patronN.match(nombre):
            comprobar = True
        else:
            print("--- Ese nombre no es válido.")
    return nombre


def comprobarTelefono():
    """
    Función que comprueba que el teléfono introducido por teclado coincida con el formato que se establece en la
    variable patronT. Mientras que no coincida, se repetirá el bucle y no saldrá.
    :return: string con un teléfono.
    """
    comprobar = False
    patronT = re.compile(r'^[6-7]\d{8}$')  # Debe empezar por 6 o 7 y estar seguido de 8 números más
    while not comprobar:
        telefono = input("Introduzca un teléfono: ")
        if patronT.match(telefono):
            comprobar = True
        else:
            print("--- Ese teléfono no es válido.")
    return telefono


def comprobarMail():
    """
    Función que comprueba que el email introducido por teclado coincida con el formato que se establece en la
    variable patronM. Mientras que no coincida, se repetirá el bucle y no saldrá.
    :return: string con un email.
    """
    comprobar = False
    patronM = re.compile(r'^[a-z0-9]+@[a-z0-9]+$')  # Debe contener letras o números, una arroba (@) y letras o números.
    while not comprobar:
        mail = input("Introduzca un email: ")
        if patronM.match(mail):
            comprobar = True
        else:
            print("--- Ese email no es válido.")
    return mail


def comprobarClienteHabitual():
    """
    Función que permite introducir si se es o no un cliente habitual, recogiendo para ello una cadena de caracteres que
    debe coincidir con los valores 'sí' o 'no' y transformando dicha cadena en un booleano: True para sí y False para
    no. Mientras que no se introduzcan estos valores, el bucle se repetirá.
    :return: boolean que define si es habitual o no.
    """
    comprobar, habitual = False, False
    while not comprobar:
        cliente = input("¿Es cliente habitual? ")
        if cliente.lower() == "sí":
            habitual = True
            comprobar = True
        elif cliente.lower() == "no":
            habitual = False
            comprobar = True
        else:
            print("--- Introduce sí o no.")
    return habitual


def comprobarFecha():
    """
    Función que comprueba que la fecha introducida por teclado coincida con el formato que se establece en la
    variable patronF. Mientras que no coincida, se repetirá el bucle y no saldrá.
    :return: string que contiene la fecha.
    """
    comprobar = False
    patronF = date.today().strftime('%d/%m/%Y')  # Fecha en formato dd/mm/aaaa.
    while not comprobar:
        fecha = input("Introduzca una fecha: ")
        if fecha == patronF:
            comprobar = True
        else:
            print("--- Debe introducir la fecha de hoy: {}.".format(patronF))
    return fecha


def opcion1(dic):
    """
    Función que añade al diccionario que se obtiene por parámetro clientes. Un DNI como clave y un diccionario con
    nombre, dirección, teléfono, email, cliente habitual y fecha de alta como valor para cada cliente.
    :param dic: diccionario recibido por parámetro.
    :return: dict que contiene un nuevo par clave-valor con un cliente.
    """
    comprobar = False
    while not comprobar:
        dni = comprobarDni()
        if dni in dic:
            print("--- Ese DNI no es posible.")
        else:
            comprobar = True
    nombreApellidos = comprobarNombreApellidos()
    direccion = input("Introduzca una dirección: ")
    telefono = comprobarTelefono()
    email = comprobarMail()
    bHabitual = comprobarClienteHabitual()
    fecha = comprobarFecha()

    cliente = {'nombre': nombreApellidos, 'dirección': direccion, 'teléfono': telefono, 'email': email,
               'habitual': bHabitual, 'fecha': fecha}
    dic.update({dni: cliente})

    print("=== Cliente introducido con éxito.")

    return dic


def opcion2(dic, dnilocal):
    """
    Función que elimina un cliente del diccionario introducido por parámetro a través del DNI introducido también por
    parámetros. Se recorre el diccionario y, si existe como clave un valor coincidente con el DNI del parámetro, se
    elimina del mismo.
    :param dic: diccionario recibido por parámetro.
    :param dnilocal: string que contiene un DNI que sirve para eliminar un cliente si existe en el diccionario.
    """
    existe = False
    for clave in dic.keys():
        if clave == dnilocal:
            existe = True
            dic.pop(clave)
            print("=== Cliente con DNI {} eliminado con éxito.".format(dnilocal))
            break
    if not existe:
        print("--- El cliente con DNI {} no existe.".format(dnilocal))


def opcion3(dic, dnilocal):
    """
    Función que muestra todos los datos de un cliente que exista dentro del diccionario introducido por parámetro. Se
    comprueba con un DNI introducido por parámetro y se devuelven los datos si existe coincidencia.
    :param dic: diccionario recibido por parámetro.
    :param dnilocal: string que contiene un DNI que sirve para mostrar un cliente si existe en el diccionario.
    """
    existe = False
    for clave, valor in dic.items():
        if clave == dnilocal:
            existe = True
            for c, v in valor.items():
                print("{}: {}".format(c, v))
    if not existe:
        print("--- El Cliente con DNI {} no existe.".format(dnilocal))


def opcion4(dic):
    """
    Función que devuelve todos los clientes existentes en el diccionario introducido por parámetro, su nombre y DNI.
    :param dic: diccionario recibido por parámetro.
    """
    existe = False
    for clave, valor in dic.items():
        existe = True
        print("{}: {}".format(valor.get('nombre'), clave))
    if not existe:
        print("=== No existen clientes en la base de datos.")


def opcion5(dic):
    """
    Función que devuelve todos los clientes que existen en el diccionario si son habituales, su nombre y DNI.
    :param dic: diccionario recibido por parámetro.
    """
    existe = False
    for clave, valor in dic.items():
        if valor.get('habitual') is True:  # No se devuelve si no es habitual.
            existe = True
            print("{}: {}".format(valor.get('nombre'), clave))
    if not existe:
        print("=== No existen clientes habituales en la base de datos.")


def opcion6():
    """
    Función que sirve para salir del menú, devolviendo un booleano igual a True, que servirá para salir del bucle del
    menú en el que se englobe esta función.
    :return: boolean igual a True.
    """
    print("Saliendo del menú.")
    return True


def menu():
    """
    Menú que contiene un listado de posibles opciones a realizar con un diccionario, que se repetirá en tanto en cuanto
    no se presione la tecla adecuada.
    """
    comprobar = False
    dni = None
    while not comprobar:
        print("=== Menú de gestión de clientes de una empresa ===")
        print()
        print("1) Añadir cliente \n"
              "2) Eliminar cliente \n"
              "3) Mostrar cliente \n"
              "4) Listar todos los clientes \n"
              "5) Listar clientes habituales \n"
              "6) Salir")
        print()
        opcion = input("=== Introduzca una opción de 1 a 6: ")
        if opcion == '1':
            opcion1(listadoClientes)
            print()
        elif opcion == '2':
            dni = comprobarDni()
            opcion2(listadoClientes, dni)
            print()
        elif opcion == '3':
            dni = comprobarDni()
            opcion3(listadoClientes, dni)
            print()
        elif opcion == '4':
            opcion4(listadoClientes)
            print()
        elif opcion == '5':
            opcion5(listadoClientes)
            print()
        elif opcion == '6':
            comprobar = opcion6()
        else:
            print("--- {} no es una opción válida.".format(opcion))
            print()


"""Ejecuta la función menu()"""
menu()
