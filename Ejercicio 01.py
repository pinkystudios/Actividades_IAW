# Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€‚', 'Dollar':'$', 'Yen':'Y'}, pregunte al usuario 
# por una divisa y muestre su si­mbolo o un mensaje de
# aviso si la divisa no esta en el diccionario.

# Diccionarios
dic_divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'Y'}

# Recoge datos del usuario
divisa = input("Introduce un tipo de divisa: ")

# Verificar si la divisa se encuentra en el diccionario
if divisa in dic_divisas:
    print(f"El simbolo del {divisa} es el siguiente: {dic_divisas[divisa]}")
else:
    print("La siguiente divisa no esta en el diccionario \nPruebe con otra")
