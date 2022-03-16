"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Encriptar. Diseñe una función
encripta(s, clave), que reciba
un string s con un mensaje y un
string con una clave de
codificación, y retorne el
mensaje codificado según la
clave leída.

"""

clave =      'ixmrklstnuzbowfaqejdcpvhyg'
abecedario = 'abcdefghijklmnopqrstuvwxyz'



def encriptar(palabra):
    cifrar = ""
    for i in palabra:
        comparar = abecedario.find(i)
        palabraCifrada = clave[comparar]
        cifrar +=palabraCifrada
    return print("Palabra encriptada: "+ cifrar)

palabra=(input("Ingresa una palabra para cifrar: "))
encriptar(palabra)


