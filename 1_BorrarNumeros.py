"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Borrar Números en string. Diseña
una función que entre un string
y devuelve el string pero sin sus
caracteres numéricos o dígitos.

"""

def BorrarBum():
    palabraSinNum = ''.join([i for i in palabra if not i.isdigit()])
    return palabraSinNum

palabra =(input("Ingresa palabra que contenga numeros: "))
print("La palabra sin numeros es: " + BorrarBum())