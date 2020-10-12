print("CAMBIO DE MONEDA")

"""Variables de entorno"""
CD_E = 0.88  # Conversión de dólar a euro. 1 dólar = .88 euros.
CE_L = 0.94  # Conversión de euros a libras. 1 euro = .94 libras.
CD_L = 0.83  # Conversión de dólar a libras. 1 dólar = .83 libras.
cambio = True


"""Menú con while y booleano"""
while cambio:
    """Variables del menú"""
    print("Introduce las monedas en minúsculas (libra, euro, dólar):")
    x = input("¿Qué moneda tienes? ")
    x1 = int(input("¿Cuántas quieres cambiar? "))
    y = input("¿A qué moneda quieres cambiar? ")
    control = False

    if x.lower() == "libra" and y.lower() == "dólar" or y.lower() == "dolar":
        y1 = (1 / CD_L) * x1
        pluralx, pluraly = "libras", "dólares"
        control = True
    elif x.lower() == "libra" and y.lower() == "euro":
        y1 = (1 / CE_L) * x1
        pluralx, pluraly = "libras", "euros"
        control = True
    elif x.lower() == "dólar" or x.lower() == "dolar" and y.lower() == "libra":
        y1 = CD_L * x1
        pluralx, pluraly = "dolares", "libras"
        control = True
    elif x.lower() == "dólar" or x.lower() == "dolar" and y.lower() == "euro":
        y1 = CD_E * x1
        pluralx, pluraly = "dolares", "euros"
        control = True
    elif x.lower() == "euro" and y.lower() == "libra":
        y1 = CE_L * x1
        pluralx, pluraly = "euros", "libras"
        control = True
    elif x.lower() == "euro" and y.lower() == "dólar" or y.lower() == "dolar":
        y1 = (1 / CD_E) * x1
        pluralx, pluraly = "euros", "dólares"
        control = True
    else:
        print("No has introducido nada que sea de provecho.")

    """Condicional que se activa solo si la variable 'control' es True, así se controlan 'pluralx' y 'pluraly'"""
    if control:
        print("Los ", x1, pluralx, "son", round(y1, 2), pluraly)

    print("¿Otro cambio? (sí/no):")
    c = input()
    if c.lower() == "no":
        cambio = False
