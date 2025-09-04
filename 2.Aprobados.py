#2. Cuenta cuántos estudiantes aprobaron todas sus asignaturas (Todas las notas >= 4.0)
import pandas as pd
import Datos as dc

from Verificador import limpiar_datos

Estudiantes = dc.Estudiantes
Estudiantes_saneados = limpiar_datos(Estudiantes)

#1. Convertir los datos de estudiantes a DataFrame
df_alumnos = pd.DataFrame(Estudiantes)

#2. Mascara que retorna True en caso que la nota sea >=4.0
mascara_aprobados = pd.DataFrame(df_alumnos["Notas"].tolist(), index=df_alumnos.index).ge(4.0).all(axis=1)

#3. Aplicacion de mascara en el DataFrame de los alumnos para filtrar
df_aprobados = df_alumnos[mascara_aprobados]

#4. Suma de la cantidad de estudiantes que poseen nota >=4.0
n_aprobados = mascara_aprobados.sum()

#5. Mostrar resultados
print("La cantidad de aprobados son: ",n_aprobados)