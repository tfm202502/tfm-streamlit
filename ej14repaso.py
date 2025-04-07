''' 
14. Lectura de datos
=========================================

DESCRIPCIÓN: Cree un programa que lea valores desde el teclado y los guarde en una lista que debe guardar al final en un fichero. 
    El programa debe terminar cuando el usuario escriba "fin".
'''


datos = []

terminadores= ["FIN", "terminar", "salir"]
dato= input ("dame un valor: ")

while dato not in terminadores:
    datos.append(dato)
    dato = input("Dame un valor: ")

filename= "resultados.txt"
with open ("resultados.txt", "w") as f:
    for valor in datos:
        f.write(valor + "\n")

  
print(f"datos guardados en el fichero {filename}")


