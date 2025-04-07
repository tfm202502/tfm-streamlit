''' 
07. Análisis de respuestas abiertas
===================================

DESCRIPCIÓN: Dada una lista de respuestas abiertas (cadenas de texto), 
    cuenta cuántas veces aparece una palabra clave como “política” o “economía”.
'''

keywords = ["política", "economía"]
respuestas = ["Me interesa la política y la economía", "La economía es importante", "Política global"]

tablaFrecuencias = {}

for respuesta in respuestas:
    palabras = respuesta.lower().split (sep=" ")
    for word in palabras:
        if word in keywords:
            tablaFrecuencias[word] = tablaFrecuencias.get(word,0) + 1

print (tablaFrecuencias)


## El resultado debe ser:
#   {'política': 2, 'economía': 2}
