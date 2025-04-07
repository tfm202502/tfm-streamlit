''' 
08. Comparación de dos datasets de encuestas
============================================

DESCRIPCIÓN: Dadas dos listas de resultados de encuestas de dos años distintos, 
    escribe un programa que compare las respuestas y muestre las diferencias.
'''

encuesta_2023 = [5, 4, 3, 5, 2, 5, 2]
encuesta_2024 = [4, 4, 3, 5, 1, 4, 3]

encuestas_comparar= []

for valor in range(len(encuesta_2023)):
    if encuesta_2023[valor] == encuesta_2024[valor]:
        encuestas_comparar.append(True)
    else:
        encuestas_comparar.append(False)

print(encuestas_comparar)

## El resultado debe ser:
#   [False, True, True, True, False, False, False]
