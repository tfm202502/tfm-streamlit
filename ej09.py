''' 
09. Limpieza de valores no válidos
============================================

DESCRIPCIÓN: Escribe un programa que limpie una lista de edades, 
    eliminando valores imposibles.
'''

edades = [35, -4, 543, 23, 42, 45, -52, 120, 94, 469, 33]

edad_minima = 0
edad_max = 125
limpio= []

for edad in edades:
    if edad >= edad_minima and edad <= edad_max:
        limpio.append (edad)

print (limpio)
## El resultado debe ser:
#   [35, 23, 42, 45, 120, 94, 33]
