"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Frecuencia de Números. Diseña
una función frecuencias(lst) en
que, dada una lista de números
naturales, devuelve un diccionario
con el número de veces que aparece
cada número en la lista dada.

"""
from statistics import mean

m = ([1,2,3,4],[1,3,5,7])

def Media(m):
    filas=len(m)
    columnas=len(m[0])

    for i in range(filas):
        promedio=mean(m[i])
        print("El promedio de la fila " , i , "es igual a: " ,promedio)
    return

Media(m)