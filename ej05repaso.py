''' 
05. Normalización de datos de encuesta
======================================

DESCRIPCIÓN: Escribe un programa que convierta las respuestas de una encuesta 
    en formato sí/no a un formato binario (1 para “Sí” y 0 para “No”).
'''

respuestas = ["Sí", "No", "Sí", "No", "No", "No", "Sí"]

respuestas_binarias = [1 if respuesta == "Sí" else 0 for respuesta in respuestas]

print(respuestas_binarias)




## El resultado debe ser:
#   [1, 0, 1, 0, 0, 0, 1]
