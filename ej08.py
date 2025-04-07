''' 
08. Comparación de dos datasets de encuestas
============================================

DESCRIPCIÓN: Dadas dos listas de resultados de encuestas de dos años distintos, 
    escribe un programa que compare las respuestas y muestre las diferencias.
'''

encuesta_2023 = [5, 4, 3, 5, 2, 5, 2]
encuesta_2024 = [4, 4, 3, 5, 1, 4, 3]
coincidencia= []


#coincidencia= [encuesta_2023 [i]] == encuesta_2024 [i] for i in range(len(encuesta_2023))
#hay ocasiones que no queda otra que trabajar con los índices, con las posiciones
for i in range (len(encuesta_2023)):
    if encuesta_2023[i] == encuesta_2024[i]:
        coincidencia.apprend(True)
    else:
        coincidencia.append(False)

print(coincidencia)



#se puede acortar:
''' 
coincidencia = []
for i in range(len(encuesta_2023)):
    coincidencia.append(encuesta_2023[i] == encuesta_2024[i])
'''



## El resultado debe ser:
#   [False, True, True, True, False, False, False]