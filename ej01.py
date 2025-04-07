'''
01. Cálculo de media y mediana de encuestas

02. Cálculo de producto de números de una lista. ESTE ES EL QUE SE VA A HACER
===========================================

DESCRIPCIÓN: Dada una lista de resultados de una encuesta (números), 
    escribe un programa que calcule la media y la mediana de esos resultados.
'''
import statistics as st

valores = [3, 4, 5, 2, 5, 5, 1]


media= st.mean(valores)
print (media)

mediana= st.median(valores)
print(mediana)

acumulado = 1

for v in valores:
    acumulado = acumulado * v

print (acumulado)



## El resultado debe ser:
#   Media: 3.5714285714285716
#   Mediana: 4
