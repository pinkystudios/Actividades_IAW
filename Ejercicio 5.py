# Escribir un programa que pregunte al usuario una cantidad a invertir
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión cada año que dura la inversión.

def operacion (años, interes, invertir):
    
    for i in range(años):
        invertir = invertir * (1 + interes/100)
        print(f"el capital ganado en el año {i+1} es: {round(invertir, 2)}")
        
invertir = int(input("Escribe la cantidad a invertir: "))
interes = int(input("Escribe el interes anual: "))
años = int(input("Escribe el numero de años: "))

operacion (años, interes, invertir)