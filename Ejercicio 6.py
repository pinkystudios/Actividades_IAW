# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla si es par o impar.

def numpar (num):
    
    if (num%2 == 0):
        print ("Tu numero es par")
    else:
        print("Tu numero es impar")

num = int(input("Introduce un numero: "))
numpar (num)