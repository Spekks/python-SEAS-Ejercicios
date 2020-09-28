# Resultado de las expresiones lógicas:

# v1 = not(False or True # True) # False
# v2 = not((False or True # True) and (False and False # False) # False) # True
# v3 = (False or True # True) and (not(False and False # False) # True) # True

v1 = not(False or True)
v2 = not((False or True) and (False and False))
v3 = (False or True) and (not(False and False))

print(v1)
print(v2)
print(v3)
