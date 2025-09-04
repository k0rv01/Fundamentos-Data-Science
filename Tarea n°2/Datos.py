import numpy as np
import pandas as pd


Estudiantes = [
    {"Nombre": "Andrea", "Notas": [2.1, 6.5, 1.3], "Edad": 22},
    {"Nombre": "Esteban", "Notas": [4.9, 5.6, 2.0], "Edad": 23},
    {"Nombre": "Martina", "Notas": [6.3, 5.0, 4.3], "Edad": 25},
    {"Nombre": "Francisco", "Notas": [4.5, 1.9, 3.9], "Edad": 22},
    {"Nombre": "Francisco", "Notas": [6.5, 3.1, 5.0], "Edad": 20},
    {"Nombre": "Fabiola", "Notas": [6.6, 1.4, 5.5], "Edad": 24},
    {"Nombre": "Lorena", "Notas": [5.8, 2.0, 5.2], "Edad": 24},
    {"Nombre": "Gonzalo", "Notas": [6.4, 3.9, 3.2], "Edad": 24},
    {"Nombre": "Felipe", "Notas": [5.9, 1.4, 5.0], "Edad": 21},
    {"Nombre": "Álvaro", "Notas": [5.1, 5.9, 4.4], "Edad": 25},
    {"Nombre": "Josefa", "Notas": [2.3, 4.7, 3.1], "Edad": 27},
    {"Nombre": "Gonzalo", "Notas": [5.1, 1.1, 3.0], "Edad": 25},
    {"Nombre": "Esteban", "Notas": [5.6, 5.1, 2.0], "Edad": 23},
    {"Nombre": "Rodrigo", "Notas": [4.0, 6.7, 6.8], "Edad": 19},
    {"Nombre": "Óscar", "Notas": [1.3, 2.6, 1.2], "Edad": 27},
    {"Nombre": "Óscar", "Notas": [4.5, 2.3, 3.8], "Edad": 22},
    {"Nombre": "Florencia", "Notas": [4.9, 2.2, 2.3], "Edad": 24},
    {"Nombre": "Constanza", "Notas": [1.2, 2.6, 1.3], "Edad": 22},
    {"Nombre": "Rodrigo", "Notas": [6.0, 4.5, 1.6], "Edad": 20},
    {"Nombre": "Pablo", "Notas": [1.2, 3.4, 2.1], "Edad": 24},
    {"Nombre": "Gonzalo", "Notas": [6.0, 2.1, 3.7], "Edad": 26},
    {"Nombre": "Josefa", "Notas": [2.9, 5.7, 6.9], "Edad": 22},
    {"Nombre": "Carolina", "Notas": [1.1, 2.6, 6.5], "Edad": 20},
    {"Nombre": "Patricia", "Notas": [5.9, 5.8, 5.5], "Edad": 20},
    {"Nombre": "Rocío", "Notas": [3.5, 5.2, 6.4], "Edad": 19},
    {"Nombre": "Lorena", "Notas": [2.7, 4.0, 1.9], "Edad": 22},
    {"Nombre": "Ignacio", "Notas": [2.0, 1.2, 6.5], "Edad": 21},
    {"Nombre": "Martina", "Notas": [3.1, 4.7, 6.7], "Edad": 19},
    {"Nombre": "Pablo", "Notas": [2.6, 2.3, 2.7], "Edad": 22},
    {"Nombre": "Rodrigo", "Notas": [2.7, 4.6, 1.4], "Edad": 19}
]

df_estudiantes = pd.DataFrame(Estudiantes)

print(df_estudiantes)


