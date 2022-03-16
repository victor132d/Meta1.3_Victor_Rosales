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

x = 1
lst = []

while x <= 10:
    num = int(input("Ingrese el numero " + str(x) + ":"))
    lst.append(num)
    x += 1

print("\nLista sin ordenar: "+ str(lst))

def Frecuencia(lst):

    numeros = []
    cantidad = []

    for i in range(len(lst)):
        cont = 0
        for j in lst:
            if lst[i] == j:
                cont += 1
                if (lst[i] in numeros) == False:
                    numeros.append(lst[i])
        cantidad.append(cont)

    frecc = dict(zip(numeros, cantidad))

    return print(frecc)


Frecuencia(lst)