''' 
11. Análisis de frecuencia de palabras
======================================

DESCRIPCIÓN: Dado un fichero de respuestas abiertas de encuestas, 
    escribe un programa que calcule la frecuencia de las palabras
    y muestre las diez palabras más frecuentes.
'''
with open("respuestas_encuesta.txt", "r", encoding="utf-8") as f:
    tablapalabras = {}

    # Procesamos cada línea del fichero
    for linea in f:
        # Dividimos las líneas en palabras y las pasamos a minúsculas
        for palabra in linea.lower().split():
            # Limpiamos puntuaciones si es necesario
            palabra = palabra.strip(",.?!;:\"'()[]")
            
            # Contamos la frecuencia de las palabras
            if palabra in tablapalabras:
                tablapalabras[palabra] += 1
            else:
                tablapalabras[palabra] = 1

# Ordenamos el diccionario por frecuencia en orden descendente
tabla_ordenada = sorted(tablapalabras.items(), key=lambda x: x[1], reverse=True)

# Mostramos las 10 palabras más frecuentes
print(dict(tabla_ordenada[:10]))


## El resultado debe ser:
# {'la': 328, 'el': 197, 'es': 187, 'y': 174, 'más': 144, 'que': 134, 'de': 122, 'en': 113, 'los': 103, 'me': 102}




students = ["A", "B", "C"]

for i in range (len(students)):
	print (i + 1, students[i])
     

for i in [0,1,2]:
	print ("meow")



