''' 
09. Limpieza de valores no válidos
============================================

DESCRIPCIÓN: Escribe un programa que limpie una lista de edades, 
    eliminando valores imposibles.
'''

edades = [35, -4, 543, 23, 42, 45, -52, 120, 94, 469, 33]

lista_edad= []

for edad in edades:
    if edad > 0 and edad < 100:
        lista_edad.append(edad)

print(lista_edad)

## El resultado debe ser:
#   [35, 23, 42, 45, 120, 94, 33]
