# Escribir un programa que almacene la cadena 
# de caracteres contraseña en una variable, pregunte al usuario 
# por la contraseña hasta que introduzca la contraseña correcta.

password = "p4sSw0rD"
true = False

while (not true):
    contra_secreta = input("Escribe la clave: ")
    if (password == contra_secreta):
        print("\n Bienvenido de nuevo \n")
    else:
        print ("\n la contrase�a es incorrecta \n Intentalo de nuevo \n")