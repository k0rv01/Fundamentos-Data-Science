#1. Calcula el promedio de notas de cada estudiante y determina quién tiene promedio mas alto y mas bajo
import numpy as np
import pandas as pd
import Datos as dc

from Verificador import limpiar_datos

Estudiantes = dc.Estudiantes
Estudiantes_saneados = limpiar_datos(Estudiantes)

#1. Convertir los datos de estudiantes a DataFrame
df_alumnos = pd.DataFrame(Estudiantes)

#2. Convertir en DataFrame la columna de "Notas"
notas = pd.DataFrame(df_alumnos["Notas"].tolist())

#3. Calcular el promedio de cada alumno
df_alumnos["Promedio"] = notas.mean(axis = 1).round(1)

#4. Guardar el peor y mejor promedio del curso
mejor_promedio = df_alumnos.loc[df_alumnos["Promedio"].idxmax()]
peor_promedio = df_alumnos.loc[df_alumnos["Promedio"].idxmin()]

print("\n\nLISTA DE PROMEDIO DE ESTUDIANTES")
print(df_alumnos[["Nombre", "Promedio"]])
print("\nEl estudiante con mejor promedio es", mejor_promedio["Nombre"], "con un", round(mejor_promedio["Promedio"], 1))
print("El estudiante con peor promedio es", peor_promedio["Nombre"], "con un", round(peor_promedio["Promedio"], 1))












