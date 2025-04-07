'''
01. Cálculo de media y mediana de encuestas
===========================================

DESCRIPCIÓN: Dada una lista de resultados de una encuesta (números), 
    escribe un programa que calcule la media y la mediana de esos resultados.
'''

valores = [3, 4, 5, 2, 5, 5, 1]

def mean(valores):
    media= sum(valores)/len(valores)
    # Calcular la mediana
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    
    if n % 2 == 0:  # Si la cantidad de elementos es par
        mediana = (valores_ordenados[n//2 - 1] + valores_ordenados[n//2]) / 2
    else:  # Si la cantidad de elementos es impar
        mediana = valores_ordenados[n//2]
    
    return media, mediana


media, mediana = mean(valores)
print("Media:", media)
print("Mediana:", mediana)


## El resultado debe ser:
#   Media: 3.5714285714285716
#   Mediana: 4
