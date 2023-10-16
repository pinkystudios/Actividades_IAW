# Escribir un programa que muestre por pantalla 
# la tabla de multiplicar del 1 al 10.

for j in range(1, 11):
    print(f"Tabla del {j}:\n")
    for i in range(1, 11):
        multiplos = j * i
        print(f"{j} x {i} = {multiplos}\n")