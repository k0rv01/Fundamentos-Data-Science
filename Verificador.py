def limpiar_datos(estudiantes):



#1. Lista con los estudiantes con notas procesables
    notas_limpias = []
    
#2. Aviso para la existencia de datos no validos
    excluidos = False
    
    
#3. Verificador de lista de notas vacias
    for est in estudiantes:
        notas = est.get("Notas", None)
        if not notas:
            excluidos = True
            continue

        notas_limpias = []
        
#4. Verificador de lista con notas no numericas
        for n in notas:
            try:
                n = float(n)
            except (TypeError, ValueError):
                continue
        
#5. Verificador de nota negativa
            if n < 0:
                n = abs(n)
                
#6. Verificador de nota dentro del rango
            if n < 1.0:
                n = 1.0
            elif n > 7.0:
                n = 7.0
                
#7. Ingreso de notas limpias
            notas_limpias.append(n)

#8. Exclusion de estudiante sin notas validas
        if not notas_limpias:
            excluidos = True
            continue
        
#9. Remplazo de notas originales con las saneadas
        estudiante_limpio = est.copy()
        estudiante_limpio["Notas"] = notas_limpias
        notas_limpias.append(estudiante_limpio)

    if excluidos:
        print("\n\n¡¡Algunos estudiantes fueron excluidos por datos invalidos!!")
    else:
        print("\n\n¡¡Todos los estudiantes se encuentran con datos validos!!")



    return notas_limpias

