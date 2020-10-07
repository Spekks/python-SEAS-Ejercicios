# n1 a n9 son los números, suma es la suma de un lado, contador cuenta las soluciones que cumplen la condición

contador = 0
for n1 in range(1, 10):
    for n2 in range(1, 10):
        if n1 != n2:
            for n3 in range(1, 10):
                if n3 != n1 and n3 != n2:
                    for n4 in range(1, 10):
                        if n4 != n1 and n4 != n2 and n4 != n3:
                            suma = n1 + n2 + n3 + n4  # suma de los números del primer lado. Comienza el segundo lado
                            for n5 in range(1, 10):
                                if n5 != n1 and n5 != n2 and n5 != n3 and n5 != n4:
                                    for n6 in range(1, 10):
                                        if n6 != n1 and n6 != n2 and n6 != n3 and n6 != n4 and n6 != n5:
                                            for n7 in range(1, 10):
                                                cumple1 = (n7 != n1) and (n7 != n2) and (n7 != n3) and (n7 != n4) and \
                                                          (n7 != n5) and (n7 != n6)
                                                if cumple1 & suma == n4 + n5 + n6 + n7:
                                                    for n8 in range(1, 10):
                                                        cumple2 = (n8 != n1) and (n8 != n2) and (n8 != n3) and (n8 !=
                                                                                                                n4)
                                                        cumple3 = (n8 != n5) and (n8 != n6) and (n8 != n7)
                                                        if cumple2 and cumple3:
                                                            for n9 in range(1, 10):
                                                                cumple4 = (n9 != n1) and (n9 != n2) and (n9 != n3) and \
                                                                          (n9 != n4)
                                                                cumple5 = (n9 != n5) and (n9 != n6) and (n9 != n7) and \
                                                                          (n9 != n8)
                                                                if cumple4 and cumple5 and (suma == n7 + n8 + n9 + n1):
                                                                    print("Secuencia: ", n1, " ", n2, " ", n3, " ", n4,
                                                                          " ", n5, " ", n6, " ", n7, " ", n8, " ", n9)
