students = ["A", "B", "C"]
for i in range (len(students)):
	print (students[i])


for i in range (len(students)):
	print (i + 1, students[i])
	

''' Lee los datos de un archivo y los devuelve en una lista.

    Args:
        nombre_archivo (str): Nombre del archivo a cargar.

    Returns:
        list: Lista con las respuestas. Cada elemento de la lista es una respuesta.
    '''

 ''' Devuelve un diccionario con la frecuencia de temas encontrados en las respuestas.
    
    Args:
        respuestas (list): Lista de respuestas.
        temas (list): Lista de temas a analizar.
        
    Returns:
        dict: Diccionario con la frecuencia de temas.        
    '''
  """ Devuelve un diccionario con el número de palabras positivas y negativas encontradas en las respuestas. 
    Args:
        respuestas (list): Lista de respuestas.
        palabras_positivas (list): Lista de palabras positivas.
        palabras_negativas (list): Lista de palabras negativas.

    Returns:
        dict: Diccionario con la clasificación de sentimientos.
    """
    ''' Muestra un gráfico de barras con los datos proporcionados.

    Args:
        datos (dict): Diccionario con los datos a graficar.
        titulo (str): Título del gráfico
    
    Returns:
        None
    '''
