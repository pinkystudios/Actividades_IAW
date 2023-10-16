# Escribir un programa en el que se pregunte al usuario por una frase y
# una letra, y muestre por pantalla el número de veces que aparece 
# la letra en la frase.

# Solicitud de parametros al usuario
frase = input("Introduce una frase: ")
letra = input("Bien, ahora indica que letra quieres contar: ")

contador = 0 # Activamos el contador para las letras

for caracter in frase:
    if caracter == letra:
        contador += 1
        
print(f"la letra '{letra}' aparece una cantidad de {contador} veces")