"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Escribe la función uniqueNumbers()
usando la estructura while que lea
números enteros del teclado hasta
que obtenga 5 números distintos
(no repetidos) y devuelva una lista
 con estos números distintos.

"""


def repeat():
    sinRepetir = []
    x = 1
    while x <= 5:
        num = int(input("Ingrese el numero "+ str(x) + ":"))
        if num not in sinRepetir:
            sinRepetir.append(num)
            x += 1
        else:
            print("Numero repetido, inténte con otro")
    return print('Lista sin repetir: ', sinRepetir)

repeat()
