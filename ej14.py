''' 
14. Lectura de datos
=========================================

DESCRIPCIÓN: Cree un programa que lea valores desde el teclado y los guarde en una lista que debe guardar al final en un fichero. 
    El programa debe terminar cuando el usuario escriba "fin".
'''


datos = []

terminadores= ["FIN", "terminar," "salir"]
dato= input ("dame un valor: ")

while dato not in terminadores:
    datos.append(dato)
    dato = input("Dame un valor: ")

with open ("resultados.txt", "w") as f:
    for dato in datos:
        f.write(datos)

for dato in datos:  
    print(datos)


datos = []

dato = input("Dame un valor por fa plis")
while dato != "fin" :
    datos.append(dato)
    dato = input("Dame un valor por fa plis")

print(datos)