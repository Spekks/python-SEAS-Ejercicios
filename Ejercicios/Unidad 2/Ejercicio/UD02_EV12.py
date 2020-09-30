# Determinar la diferencia de código existente en código ASCII entre los carácteres en mayúscula y en minúscula. Poner
# como ejemplo el código del carácter 'A' y el 'a'.

tTuplaMi, tTuplaMa = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'), \
                     ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')

for i in range(0, 10):
    print(ord(tTuplaMi[i]), ord(tTuplaMa[i]), sep=" - ")

