"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Positivos y Negativos. Diseña
una función PositNegat(lst)
que reciba una lista, lst,
y devuelva 2 listas, una con
los Valores positivos o 0 y
otra con los negativos.

"""

x = 1
nums = []

while x <= 5:
    num = int(input("Ingrese el numero " + str(x) + ":"))
    nums.append(num)
    x += 1

print("\nLista sin ordenar: "+ str(nums))

def PositNegat():
    positivo = []
    negativo = []

    for i in nums:

        if i >= 0:
            positivo.append(i)
        else:
            negativo.append(i)
    listas = [positivo, negativo]
    return print(listas)

print("\nListas ordenadas:")
PositNegat()
