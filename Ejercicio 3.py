# Ejercicio 2
# Solicitar al usuario que ingrese dos números 
# y mostrar cuál de los dos es menor. 
# considerar el caso en que ambos números son iguales.

def esmayor (num1, num2):

    if num1 > num2:
        print("el numero 1 es mayor al numero 2")
    elif num1 == num2:
        print("Ambos numeros son iguales")
    else:
        print("El numero 2 es mayor al numero 1")
        
num1 = int(input ("Introduce un numero: "))
num2 = int(input ("Introduce otro numero: "))

esmayor (num1, num2)