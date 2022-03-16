"""
Rosales Blanco Victor Ernesto
Creado: 06/03/2022
Ultima modificacion: 06/03/22

Temperaturas de ciudades. Un
diccionario guarda las
temperaturas mínimas de los
3 primeros meses del año de
distintas ciudades

"""
from statistics import mean

dic = {'Londres': [3.4, 6.3, 10.5], 'Oslo': [-3.8, -5.0, 4.2], 'Rennes': [2.5, 3.1, 12.3]}

resultado={}



def minimas(dic):
    minimos=0
    for key in dic:
        #print(dic[key])
        minimos= min(dic[key])
        resultado[key]=minimos
        #for item in dic[key]:
        # print item
    return print("Temperatura mas baja de cada ciudad: ", resultado)

def minimaTotal(dic):
    minimos = 0
    minimoFinal=0
    for key in dic:
        minimos = min(dic[key])
        resultado[key] = minimos
        minimoFinal=min(resultado.values())
        res = [key for key in resultado if resultado[key] == minimoFinal]
    return print("Temperatura Temperatura mas baja: ", {str(res):minimoFinal})

def media(dic):
    minimos = 0
    for key in dic:
        # print(dic[key])
        minimos = mean(dic[key])
        resultado[key] = "{0:.2f}".format(minimos)
        # for item in dic[key]:
        # print item
    return print("Temperatura mas baja de cada ciudad: ", resultado)

minimas(dic)
minimaTotal(dic)
media(dic)