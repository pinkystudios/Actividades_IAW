# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
# contenido del diccionario.


# Creamos el diccionario
inf_personal = {}

# Definimos una lista con las claves a solicitar
datos = ["nombre", "edad", "sexo", "telefono", "email"]

# Recogemos los datos del usuario y los añadimos a los datos anteriores
for key in datos:
    valor = input(f"Indica tu {key}: ")
    inf_personal[key] = valor
    print(f"Tus datos actualizados son: {inf_personal}")