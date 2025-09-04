#3. ¿Cuál es la nota más frecuente (moda) considerando todas las notas de todos los estudiantes?
import pandas as pd
import numpy as np
import Datos as dc

from Verificador import limpiar_datos

Estudiantes = dc.Estudiantes
Estudiantes_saneados = limpiar_datos(Estudiantes)


# 1. Obtener la columna de notas de los estudiantes
lista_notas = [e["Notas"] for e in Estudiantes]

# 2. Crear un arreglo de numpy en 1D
arr_notas = np.array(lista_notas, dtype=float).ravel()

# 3.Establecer las notas en un decimal
arr_notas = np.round(arr_notas, 1)

# 4. Encontrar el valor mas frecuente
numeros, contador = np.unique(arr_notas, return_counts=True)
moda = float(numeros[np.argmax(contador)])

#5. Mostrar resultados
print("La nota mas frecuente entre los alumnos es ", moda)




