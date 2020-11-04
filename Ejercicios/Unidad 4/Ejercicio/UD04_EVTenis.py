#  Ejercicio marcador de tenis. Unidad 4.
import time
from random import randint

#  Variables:
FIRST_BALL = 15
THIRD_BALL = 10


def mostrarResultado(j):
    print("Marcador: ")
    time.sleep(0.5)
    for c, v in j.items():
        print("{}: {}".format(c, v))


def mostrarResultadoP(p):
    for c, v in p.items():
        print("{}".format(c))
        print("------")
        for clave, valor in v.items():
            print("{}: {}".format(clave, valor))
        print("------")
    print("Partido finalizado")


def juego(jj1, jj2, sett):
    juego1 = []
    juego2 = []
    cCuarenta1 = []
    cCuarenta2 = []
    bJuego = False
    bJuego2 = False

    print("Juego entre {} y {}".format(jj1, jj2))
    while not bJuego:
        punto = randint(0, 10)
        if punto >= 5:
            if len(juego1) < 2:
                juego1.append(FIRST_BALL)
                time.sleep(0.5)
            else:
                juego1.append(THIRD_BALL)
                time.sleep(0.5)
        else:
            if len(juego2) < 2:
                juego2.append(FIRST_BALL)
                time.sleep(0.5)
            else:
                juego2.append(THIRD_BALL)
                time.sleep(0.5)
        print("{} - {}".format(juego1, juego2))
        time.sleep(0.5)

        if len(juego1) == 3 and len(juego2) == 3:
            while not bJuego2:
                punto = randint(0, 10)
                if punto >= 5:
                    cCuarenta1.append(1)
                    print("Tie break: {} - {}".format(cCuarenta1, cCuarenta2))
                    time.sleep(0.5)
                else:
                    cCuarenta2.append(1)
                    print("Tie break: {} - {}".format(cCuarenta1, cCuarenta2))
                    time.sleep(0.5)

                if len(cCuarenta1) - len(cCuarenta2) == 2:
                    bJuego = True
                    bJuego2 = True
                    sett[jj1].append(1)
                    print("Juego para {}".format(jj1))
                    time.sleep(0.5)
                elif len(cCuarenta2) - len(cCuarenta1) == 2:
                    bJuego = True
                    bJuego2 = True
                    sett[jj2].append(1)
                    print("Juego para {}".format(jj2))
                    time.sleep(0.5)
        elif len(juego1) >= 3 and len(juego1) - len(juego2) >= 2:
            sett[jj1].append(1)
            bJuego = True
            print("Juego para {}".format(jj1))
            time.sleep(0.5)
        elif len(juego2) >= 3 and len(juego2) - len(juego1) >= 2:
            sett[jj2].append(1)
            bJuego = True
            print("Juego para {}".format(jj2))
            time.sleep(0.5)
    mostrarResultado(sett)
    time.sleep(0.5)


def sets(j1, j2):
    setTemp = {j1: [], j2: []}
    bCheck = False
    while not bCheck:
        juego(j1, j2, setTemp)
        for valor in setTemp.values():
            if len(valor) == 6:
                bCheck = True
                print("Set finalizado")
    return setTemp


def match():
    jugador1 = input("Jugador 1: ")
    jugador2 = input("Jugador 2: ")
    partido = {"set1": {}, "set2": {}, "set3": {}}
    for key in partido.keys():
        partido[key] = sets(jugador1, jugador2)

    mostrarResultadoP(partido)


match()
