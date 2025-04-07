''' 
13. Análisis de frecuencia de respuestas
=========================================

DESCRIPCIÓN: Dado un fichero de respuestas abiertas de encuestas, 
    escribe un programa que calcule la frecuencia de dichas respuestas
    y muestre las diez respuestas más frecuentes.
'''

with open ("respuestas_encuestas.txt", "r", encoding='utf-8') as file:
    respuestas= [line.strip() for line in file] # con el strip elimina los saltos de línea (\n) al final de cada línea 

frec_respuestas={}

for frases in respuestas:
    respuesta=frases.lower()
    if respuesta in frec_respuestas:
        frec_respuestas[respuesta]= frec_respuestas[respuesta] + 1
    else:
        frec_respuestas[respuesta] = 1

ordenar= sorted(frec_respuestas.items(),key=lambda x:x[1], reverse= True)

print(dict(ordenar [:10]))