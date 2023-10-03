# Solicitar al usuario que ingrese tres numeros y 
# mostrar cual es el mayor de los tres.

def esmayor (num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        print("el numero 1 es el mayor")
    elif num2 >= num1 and num2 >= num3:
        print("El numero 2 es el mayor")
    elif num3 >= num1 and num3 >= num2:
        print("El numero 3 es el mayor")
        
num1 = int(input ("Introduce el numero 1: "))
num2 = int(input ("Introduce el numero 2: "))
num3 = int(input ("Introduce el numero 3: "))

esmayor (num1, num2, num3)