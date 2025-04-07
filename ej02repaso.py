''' 
02. Clasificación de opiniones
==============================

DESCRIPCIÓN: Dada una lista de opiniones cualitativas (e.g., “Bueno”, “Malo”, “Regular”), 
    escribe un programa que cuente cuántas opiniones de cada tipo hay.
'''

opiniones = ["Bueno", "Malo", "Regular", "Bueno", "Bueno", "Malo"]

palabras={}

for opinion in opiniones:
    if opinion in palabras:
        palabras[opinion] = palabras [opinion] + 1
    else:
        palabras[opinion] = 1

for palabr, valor in palabras.items(): #para el key, value en palabras que es el diccionario. NECESARIO EL ITEMS PARA CLAVE-VALOR
    print(f"{palabr}: {valor}")


'''Se utiliza un diccionario conteo_opiniones para almacenar la cantidad de cada tipo de opinión.
Se recorre cada elemento de la lista opiniones. Si la opinión ya está en el diccionario, se incrementa su valor. Si no, se añade al diccionario con un valor inicial de 1.
Finalmente, se imprimen las opiniones y su cantidad.
'''
'''items() es un método del diccionario que devuelve una vista de pares clave-valor
Usar .items() es necesario para obtener tanto las claves como los valores del diccionario en cada iteración.
Sin .items(), solo podrías iterar sobre las claves del diccionario, no sobre los valores.
'''



## El resultado debe ser:
#   Bueno: 3
#   Malo: 2
#   Regular: 1
