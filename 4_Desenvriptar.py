"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Desencriptar. Diseña una función
desencripta(s, clave) que realice
la función inversa a la función
anterior, es decir, reciba un string
s y una clave y realice la
desencriptación del mensaje en el
string devolviendo la cadena desencriptada.

"""

clave =      'ixmrklstnuzbowfaqejdcpvhyg'
abecedario = 'abcdefghijklmnopqrstuvwxyz'



def desEncriptar(palabra):
    decifrar = ""
    for i in palabra:
        comparar = clave.find(i)
        palabraDecifrada = abecedario[comparar]
        decifrar +=palabraDecifrada
    return print("Palabra Desencriptada: "+ decifrar)

palabra=(input("Ingresa una clave para decifrar: "))
desEncriptar(palabra)

