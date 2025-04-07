''' 
03. Agrupación de datos por categorías
======================================

DESCRIPCIÓN: Dado un conjunto de datos de respuestas de encuestas con categorías de edad (e.g., “18-25”, “26-35”), 
    crea un programa que agrupe y cuente cuántas personas pertenecen a cada rango de edad.
'''

edades = ["18-25", "26-35", "18-25", "36-45", "18-25", "26-35", "46-55", "18-25"]

grupo_edad= {}

for edad in edades:
    if edad in grupo_edad:
        grupo_edad [edad] = grupo_edad[edad] +1
    else:
        grupo_edad[edad]= 1



for edad,valor in grupo_edad.items():
    print(f"{edad}: {valor}")







## El resultado debe ser:
#   18-25: 4
#   26-35: 2
#   36-45: 1
#   46-55: 1
