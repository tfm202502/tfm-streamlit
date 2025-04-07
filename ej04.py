''' 
04. Análisis de frecuencia de palabras
======================================

DESCRIPCIÓN: Dada una lista de respuestas abiertas de encuestas, 
    escribe un programa que calcule la frecuencia de las palabras.
'''

respuestas = ["La política me interesa", "La economía es clave", "Política global", "Economía y política son estratégicas"]

tablaPalabras={}

for frase in respuestas:
    for palabra in frase:
        if palabra in tablaPalabras:
            tablaPalabras[palabra] = tablaPalabras[palabra] +1
        else:
            tablaPalabras[palabra] =1

print(tablaPalabras)



for frase in respuestas:
    listaPalabras =frase.lower().split(sep=" ")
    for palabra in listaPalabras:
        if palabra in tablaPalabras:
            tablaPalabras[palabra] = tablaPalabras[palabra] +1
        else: tablaPalabras[palabra] = 1

print(tablaPalabras)

## El resultado debe ser:
#   {'la': 2, 'política': 3, 'me': 1, 'interesa': 1, 'economía': 2, 'es': 1, 'clave': 1, 'global': 1, 'y': 1, 'son': 1, 'estratégicas': 1}
