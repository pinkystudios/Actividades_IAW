# Para tributar un determinado impuesto se debe ser mayor de 16 años y 
# tener unos ingresos iguales o superiores a 1000 € mensuales.
# Escribir un programa que pregunte al usuario su edad y sus ingresos
# mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def puede_tributar (edad, ingresos):
    
    if edad >= 16 and ingresos >= 1000:
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")
    
edad = int(input("¿Cuantos años tienes?: "))
ingresos = int(input("¿Cuales son tus ingresos mensuales?: "))
puede_tributar (edad, ingresos)