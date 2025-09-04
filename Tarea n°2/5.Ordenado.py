#5. Entrega un listado ordenado (de mayor a menos) de los estudiantes según su promedio

import pandas as pd
import numpy as np
import Datos as dc

from Verificador import limpiar_datos

Estudiantes = dc.Estudiantes
Estudiantes_saneados = limpiar_datos(Estudiantes)

#1. 
df_alumnos = pd.DataFrame(Estudiantes)

#2. Calcular promedio de cada estudiante
df_alumnos["Promedio"] = df_alumnos["Notas"].apply(lambda notas: sum(notas) / len(notas))

#3. Ordenar de mayor a menor segun el promedio
df_lista_alumnos = df_alumnos.sort_values(by="Promedio", ascending=False)[["Nombre","Promedio"]]
df_lista_alumnos = round(df_lista_alumnos, 1)

#4. Mostrar resultados
print("\n\nLISTA DE PROMEDIO DE CADA ALUMNO")
print(df_lista_alumnos)