# ¿Cuál es el resultante de dividir?:
#   - Un int entre un int.
#   - Un long entre un int.
#   - Un float entre un int.
#   - Un complex entre un float.
#   ------------------------------

iNum, iNum2, fNum, cNum = 3, 2, 12.9, 45+1j

# Un int entre un int. # float
print(type(iNum/iNum2), iNum/iNum2, sep=", ")
print(type(iNum//iNum2), iNum//iNum2, sep=", ")
print(type(iNum % iNum2), iNum % iNum2, sep=", ")

# Un long entre un int. # float

# Un float entre un int. # float
print(type(iNum/fNum))

# Un complex entre un float. # complex
print(type(fNum/cNum))
