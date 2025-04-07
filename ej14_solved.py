''' 
14. Lectura de datos
=========================================

DESCRIPCIÓN: Cree un programa que lea valores desde el teclado y los guarde en una lista que debe guardar al final en un fichero. 
    El programa debe terminar cuando el usuario escriba "fin".
'''


datos = []   # Lista para almacenar los valores que nos dé el usuario por teclado
lectura = input("Introduce el valor: ")

while lectura != "fin":  # Mientras el usuario no escriba "fin", seguimos pidiendo
    datos.append(lectura)
    lectura = input("Introduce el valor: ")

## si en lugar de únicamente fin, queremos que el programa termine con "FIN", "Fin", "fIn", "fIN",...
## podemos hacer lo siguiente:
# while lectura.lower() != "fin":  

## si queremos tener varias palabras que terminen el programa, podemos hacer lo siguiente:
# while lectura.lower() not in ["fin", "end", "salir", "exit"]: 

# cuando el usuario escriba "fin" (y termine el bucle), guardamos los datos en un fichero
filename = "datos.txt"
with open("datos.txt", "w") as f:
    for valor in datos:
        f.write(valor + "\n")

print(f"Datos guardados en el fichero {filename}")

