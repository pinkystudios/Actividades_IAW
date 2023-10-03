# Ejercicio 1
# Solicitar al usuario un número. 
# Si el número es el 1000, 
# imprimir "Ganaste un premio".

def premio (num):

    if (num == 1000):
        print("Ganaste un premio")
    else:
        print("No ganaste nada")

num = int(input ("Introduce un numero: "))
premio (num)