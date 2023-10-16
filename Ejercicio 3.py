# Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 
# hasta ese número separados por comas.

def numero (positivo):
    
    for i in range(1, positivo+1, 2):
        print(i, end=", ")
        
positivo = int(input("Escribe un numero positivo: "))
numero (positivo)