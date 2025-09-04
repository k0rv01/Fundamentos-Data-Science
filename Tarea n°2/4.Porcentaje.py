#4. ¿Qué porcentaje de estudiantes tiene al menos una nota bajo 4.0?
import pandas as pd
import numpy as np
import Datos as dc

from Verificador import limpiar_datos

Estudiantes = dc.Estudiantes
Estudiantes_saneados = limpiar_datos(Estudiantes)

#1. Convertir los datos de estudiantes a DataFrame
df_alumnos = pd.DataFrame(Estudiantes)

#2. Calcular que estudiantes tienen nota < 4
df_alumnos["Menor_4"] = df_alumnos["Notas"].apply(lambda notas: any(n<4 for n in notas))

#3. Calcular porcentaje
porcentaje = df_alumnos["Menor_4"].mean() * 100
porcentaje = round(porcentaje,1)

#4. Mostrar resultados
print("EL porcentaje de estudiantes con nota inferior a 4 es del %",porcentaje)
