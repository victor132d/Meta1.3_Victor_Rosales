"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Contar Mayusculas y minusculas.
Diseña una función que cuente el
número de mayúsculas y minúsculas
de un texto que entra como un string.

"""

def ContarMayMin(palabra):
    May = 0
    Min = 0
    for i in palabra:
        if i.isupper():
            May +=1
        elif i.islower():
            Min +=1

    return print("La palabra contiene " + str(Min) + " minusculas y " + str(May) + " mayusculas")


palabra =(input("Ingresa palabra que contenga mayusculas y minusculas: "))
ContarMayMin(palabra)


