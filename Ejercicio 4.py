# Escribir un programa que pida al usuario un número entero positivo
# y muestre por pantalla la cuenta atrás desde ese número hasta cero 
# separados por comas.

def numero (positivo):
    
    for i in range(positivo, 0, -1):
        print(i, end=", ")
        
positivo = int(input("Escribe un numero positivo: "))
numero (positivo)