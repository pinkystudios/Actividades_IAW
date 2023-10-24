# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de
# un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
# créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus
# créditos. Al final debe mostrar también el número total de créditos del curso.


# Creamos el diccionario
cred_asignaturas = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}

# Mostramos los creditos que tiene cada asignatura
for asignatura, creditos in cred_asignaturas.items():
    print(f"la asignatura de {asignatura} tiene {creditos} creditos.")

# Calculamos el valor total de creditos
total_cred = sum(cred_asignaturas.values())
print(f"El total del curso es {total_cred} creditos")