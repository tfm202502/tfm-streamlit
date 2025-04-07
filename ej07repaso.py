''' 
07. Análisis de respuestas abiertas
===================================

DESCRIPCIÓN: Dada una lista de respuestas abiertas (cadenas de texto), 
    cuenta cuántas veces aparece una palabra clave como “política” o “economía”.
'''

keywords = ["política", "economía"]
respuestas = ["Me interesa la política y la economía", "La economía es importante", "Política global"]

clave={}

for frase in respuestas: #para la frase en respuestas
    palabras=frase.lower().split(sep= " ")  #tener en cuenta que aqúi cambia la variable frase por palabras, entonces trabajamos con palabras
                                            #esto lo hacemos para que la frase esté en minúscula y teniendo en cuenta las separaciones
    for palabra in palabras: #para la palabra en palabras que es en frase
        if palabra in keywords: #si la palabra está en las keywords
            clave[palabra] = clave.get(palabra,0)+1 

print(clave)


## El resultado debe ser:
#   {'política': 2, 'economía': 2}
