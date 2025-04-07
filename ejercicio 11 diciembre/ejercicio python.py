import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import os

# Ruta al archivo
archivo = "C:\Users\Luz\OneDrive\Desktop\Máster\Fundamentos de Programación Aplicada al Análisis Social\Python\ejercicio 11 diciembre\datos_curva_tarea.csv"

# Verificar si el archivo existe
if os.path.exists(archivo):
    print("El archivo existe.")
else:
    print("El archivo no se encuentra. Verifica la ruta.")