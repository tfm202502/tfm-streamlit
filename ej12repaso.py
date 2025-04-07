''' 
11. Análisis de frecuencia de palabras
======================================

DESCRIPCIÓN: A partir de los resultados del ejercicio anterior, cree un histograma de las palabras más frecuentes.
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
print(dict(tabla_ordenada[:10]))

diez_tabla= dict(tabla_ordenada[:10]) #las metemos en una variable para que sea más fácil trabajar

import matplotlib.pyplot as plt

palabras = list(diez_tabla.keys()) #lo pasamos a lista
frecuencias = list(diez_tabla.values()) #lo pasamos a lista

# Crear un gráfico de barras
plt.bar(palabras, frecuencias, color='skyblue', edgecolor='black')

# Agregar título y etiquetas
plt.title('Las 10 palabras más frecuentes')
plt.xlabel('Palabras')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para que se vean mejor
plt.show()
