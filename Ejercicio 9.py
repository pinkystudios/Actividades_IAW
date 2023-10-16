# Escribir un programa que pida al usuario una palabra y luego muestre 
# por pantalla una a una las letras de la palabra introducida 
# empezando por la última.

# Solicitud de parametros al usuario
def palabra(word):
        

    for i in range(len(word)-1, -1, -1):
        print(word[i], end=", ")
 
word = input("Introduce una palabra: ")
palabra(word)