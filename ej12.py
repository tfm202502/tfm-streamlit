''' 
11. Análisis de frecuencia de palabras
======================================

DESCRIPCIÓN: A partir de los resultados del ejercicio anterior, cree un histograma de las palabras más frecuentes.
'''



import matplotlib.pyplot as plt


import os
cwd = os.getcwd()

# Ruta del fichero con los datos
filename = cwd+"/02-python-inicio/02-python-inicioSoluciones/respuestas_encuesta.txt"
with open(filename) as file:
    respuestas = [line for line in file]


tablaFrecuencias = {}  # Creo un diccionario para guardar las frecuencias

for respuesta in respuestas:
    for palabra in respuesta.lower().split():
        tablaFrecuencias[palabra] = tablaFrecuencias.get(palabra,0)+1


# Creo un diccionario ordenado descendentemente en función de los valores, no de las claves
# para crear la gráfica, me viene mejor tener un diccionario en lugar de una lista!
tablaFrecuencias_sorted = {k: v for k, v in sorted(tablaFrecuencias.items(), key=lambda item: item[1], reverse=True)}

# creo otro diccionario sólo con los más frecuentes
num_palabras_frecuentes = 10
mas_frecuentes = {k:v for k,v in list(tablaFrecuencias_sorted.items())[:num_palabras_frecuentes]}
print(mas_frecuentes)


# A continuación, creo la gráfica
import matplotlib.pyplot as plt   # importo el paquete necsario

plt.bar(mas_frecuentes.keys(), mas_frecuentes.values(), color='g')
plt.title("Histograma de frecuencias de palabras")
plt.show()