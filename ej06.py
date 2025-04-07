''' 
06. Limpieza de datos
=====================

DESCRIPCIÓN: Escribe un programa que limpie una lista de respuestas sí/no 
    eliminando valores nulos, espacios en blanco y respuestas vacías.
'''

respuestas = ["Sí", "", "No", "   ", "Sí", "xxxx", None]
respuestas_limpias =  []

for elemento in respuestas:
    #if elemento == "Sí" or elemento == "No":
    if elemento in ['Sí', 'No']:
        respuestas_limpias.append(elemento)

print (respuestas_limpias)




## El resultado debe ser:
#   ["Sí", "No", "Sí"]