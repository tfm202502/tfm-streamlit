''' 
02. Clasificación de opiniones
==============================

DESCRIPCIÓN: Dada una lista de opiniones cualitativas (e.g., “Bueno”, “Malo”, “Regular”), 
    escribe un programa que cuente cuántas opiniones de cada tipo hay.
'''

opiniones = ["Bueno", "Malo", "Regular", "Bueno", "Bueno", "Malo"]

contadores = {}


## El resultado debe ser:
#   Bueno: 3
#   Malo: 2
#   Regular: 1

for opinion in opiniones:
    if opinion in contadores: 
        contadores[opinion] = contadores [opinion] +1
    else:
        contadores [opinion] =1
for cont, valor in contadores.items():
    print(f"{cont}: {valor}")


#también se puede hacer
for valor in opiniones:
    contadores[valor]= contadores.get(valor, 0)
