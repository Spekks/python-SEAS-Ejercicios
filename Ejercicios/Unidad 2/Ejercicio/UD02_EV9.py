# ¿Cuál es el resultado de multiplicar?
#   - int y long.
#   - long y long.
#   - int y float.
#   - float entre complex.
#   ---------------------------

iNum, lNum, fNum, cNum = 3, 99, 2e16, 98 + 45j

print(type(lNum))

#   - int y long -> long.
print(iNum * lNum, type(iNum * lNum), sep=", ")

#   - long y long -> long.
print(lNum * lNum, type(lNum * lNum), sep=", ")

#   - int y float -> float.
print(iNum * fNum, type(iNum * fNum), sep=", ")

#   - float entre complex -> complex.
print(fNum * cNum, type(fNum * cNum), sep=", ")
