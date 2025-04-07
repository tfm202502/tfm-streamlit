''' 
06. Limpieza de datos
=====================

DESCRIPCIÓN: Escribe un programa que limpie una lista de respuestas sí/no 
    eliminando valores nulos, espacios en blanco y respuestas vacías.
'''

respuestas = ["Sí", "", "No", "   ", "Sí", "xxxx", None]

validas=[]

for respuesta in respuestas:
    if respuesta == "Sí" or respuesta == "No":
        validas.append(respuesta)
        
print(validas)




## El resultado debe ser:
#   ["Sí", "No", "Sí"]
