''' 
11. Análisis de frecuencia de palabras
======================================

DESCRIPCIÓN: Dado un fichero de respuestas abiertas de encuestas, 
    escribe un programa que calcule la frecuencia de las palabras
    y muestre las diez palabras más frecuentes.
'''


with open ("respuestas_encuesta.txt", "r", encoding="utf-8") as file:
    respuestas= [line for line in file]
    
frec_pal={}

for frase in respuestas:
    respuesta=frase.lower().split(" ")
    for palabra in respuesta:
        if palabra in frec_pal:
            frec_pal[palabra]= frec_pal[palabra]+1
        else:
            frec_pal[palabra]=1


tabla_ordenada = sorted(frec_pal.items(), key=lambda x: x[1], reverse=True) #sorted ordena las palabras; items clave:valor, no olvidar

# Mostramos las 10 palabras más frecuentes
print(dict(tabla_ordenada[:10])) #lo que hace es crear un diccionario con las 10 más frecuenctes

print (frec_pal)


## El resultado debe ser:
# {'la': 328, 'el': 197, 'es': 187, 'y': 174, 'más': 144, 'que': 134, 'de': 122, 'en': 113, 'los': 103, 'me': 102}