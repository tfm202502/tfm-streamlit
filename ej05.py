''' 
05. Normalización de datos de encuesta
======================================

DESCRIPCIÓN: Escribe un programa que convierta las respuestas de una encuesta 
    en formato sí/no a un formato binario (1 para “Sí” y 0 para “No”).
'''

respuestas = ["Sí", "No", "Sí", "No", "No", "No", "Sí"]

respuestas_bin=[]

for respuesta in respuestas:
    if respuesta == "Sí":
        respuestas_bin.append(1)
        #print (1, respuesta)
    elif respuesta == "No":
        respuestas_bin.append(0)
        #print (0, respuesta)
   # else: si no estuviese lo demás se pondría esto
       # print("OTRA COSA")

print(respuestas_bin)

## El resultado debe ser:
#   [1, 0, 1, 0, 0, 0, 1]
