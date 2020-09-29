# Definir dos conjuntos: X1 = {a, b, c, d} y X2 = {a, c, f, g} y escribir los resultados siguientes:
#   - Los conjuntos iniciales.
#   - Los ensayos de pertenencia del elemento "a" en X1.
#   - Los conjuntos X1-X2 y X2-X1.
#   - El conjunto unión.
#   - El conjunto intersección.
#   -----------------------------------------------------

X1, X2 = {"a", "b", "c", "d"}, {"a", "c", "f", "g"}

#   - Los conjuntos iniciales.
print("Conjunto X1:", X1, "conjunto X2:", X2, sep=" ")

#   - Los ensayos de pertenencia del elemento "a" en X1.
print("a" in X1)

#   - Los conjuntos X1-X2 y X2-X1.
print("X1-X2:", X1-X2, sep=" ")
print("X2-X1:", X2-X1, sep=" ")

#   - El conjunto unión.
print("X1 | X2:", X1 | X2, sep=" ")

#   - El conjunto intersección.
print("X1 & X2:", X1 & X2, sep=" ")
