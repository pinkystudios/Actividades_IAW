# Escribir un programa que pregunte al usuario su nombre, edad, direccion 
# telefono y lo guarde en un diccionario. Después debe mostrar por pantalla el 
# mensaje <nombre> tiene <edad> años, vive en <dirección>
# y su número de teléfono es <teléfono>.

# Diccionarios
dic_datos = {}

# Recoge datos del usuario
dic_datos['nombre'] = input("Introduce tu nombre: ")
dic_datos['edad'] = input("Introduce tu edad: ")
dic_datos['direccion'] = input("Introduce tu direccion: ")
dic_datos['telefono'] = input("Introduce tu telefono: ")

# Imprimimos los datos recogidos por pantalla
print("\n" + dic_datos['nombre'] + " tiene " + dic_datos['edad'] + 
      " años, " "vive en " + dic_datos['direccion'] + 
      " y su numero de telefono es \n" + dic_datos['telefono'])