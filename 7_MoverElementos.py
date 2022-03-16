"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Mover elementos de una lista a
la derecha (Right shift). Diseña
una función mueve_derecha(lst)
(no productiva) que dada una lista,
lst, la devuelva con sus elementos
corridos hacia la derecha (y el
último de primero). Right-shift.

"""

x = 1
lst = []

while x <= 5:
    num = int(input("Ingrese el numero " + str(x) + ":"))
    lst.append(num)
    x += 1

print("\nLista sin ordenar: "+ str(lst))

def moverElementos(lst):
    lst.reverse()
    return print(lst)

print("\nLista invertida:")
moverElementos(lst)
