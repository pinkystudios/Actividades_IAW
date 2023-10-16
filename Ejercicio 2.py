# Escribir un programa que pregunte al usuario su edad y muestre 
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def numero (edad):
    
    for i in range(1, edad+1):
        print(i)
        
edad = int(input("¿Que edad tienes?: "))
numero (edad)