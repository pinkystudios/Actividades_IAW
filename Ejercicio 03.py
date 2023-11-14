# Escribir un programa que guarde en un diccionario los precios de las frutas de 
# la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por 
# pantalla el precio de ese número de kilos de fruta. Si la fruta no está en 
# el diccionario debe mostrar un mensaje informando de ello.

# Diccionarios
dic_frutas = {'Platano':1.35, 'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}

# Recoge datos del usuario
fruta = input("Indica que fruta quieres comprar: ")
peso =float(input("Indica su peso en kilogramos: "))

# Verificar si la divisa se encuentra en el diccionario
if fruta in dic_frutas:
    precio = dic_frutas[fruta] * peso
    print(f"El precio de {peso}kg de {fruta} cuesta {precio}€")
else:
    print("La siguiente fruta no esta disponible \nPruebe con otra")
