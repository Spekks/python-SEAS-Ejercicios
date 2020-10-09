lLista = [(a, b, c) for a in range(1, 20) for b in range(1, 20) for c in range(1, 20) if a**2 + b**2 == c**2]

dComp = {k: v for k in range(1, len("hola")+1) for v in "hola"}

print(dComp)
