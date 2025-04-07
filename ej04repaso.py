''' 
04. Análisis de frecuencia de palabras
======================================

DESCRIPCIÓN: Dada una lista de respuestas abiertas de encuestas, 
    escribe un programa que calcule la frecuencia de las palabras.
'''

respuestas = ["La política me interesa", "La economía es clave", "Política global", "Economía y política son estratégicas"]

frec_palabras= {}

for frase in respuestas:
    lista_palabras =frase.lower().split(sep=" ")
    for palabra in lista_palabras:
        if palabra in frec_palabras:
            frec_palabras[palabra] = frec_palabras[palabra]+1
        else:
            frec_palabras[palabra]= 1

print(frec_palabras)






## El resultado debe ser:
#   {'la': 2, 'política': 3, 'me': 1, 'interesa': 1, 'economía': 2, 'es': 1, 'clave': 1, 'global': 1, 'y': 1, 'son': 1, 'estratégicas': 1}
