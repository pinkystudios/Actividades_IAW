# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las
# facturas se almacenarán en un diccionario donde la clave de cada factura será el número
# de factura y el valor el coste de la factura. El programa debe preguntar al usuario si
# quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una
# nueva factura se preguntará por el número de factura y su coste y se añadirá al
# diccionario. Si se desea pagar una factura se preguntará por el número de factura y se
# eliminará del diccionario. Después de cada operación el programa debe mostrar por
# pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

# Diccionario para almacenar las facturas
facturas = {}

# Inicializamos las cantidades cobrada y pendiente
total_cobrado = 0
total_pendiente = 0

# Bucle para gestionar las operaciones
while True:
    print("\n--- Menú ---")
    print("1. Añadir nueva factura")
    print("2. Pagar factura existente")
    print("3. Terminar")
    
    opcion = input("Elige una opción (1/2/3): ")

    if opcion == '1':
        # Añadir una nueva factura
        num_factura = input("Introduce el número de factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[num_factura] = coste
        total_pendiente += coste

    elif opcion == '2':
        # Pagar una factura existente
        num_factura = input("Introduce el número de factura a pagar: ")
        if num_factura in facturas:
            total_cobrado += facturas[num_factura]
            total_pendiente -= facturas[num_factura]
            del facturas[num_factura]
            print(f"Factura {num_factura} pagada.")
        else:
            print(f"No se encontró ninguna factura con el número {num_factura}.")

    elif opcion == '3':
        # Terminar el programa
        break

    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")

    # Mostrar el estado actual
    print(f"\nCantidad cobrada hasta el momento: {total_cobrado}")
    print(f"Cantidad pendiente de cobro: {total_pendiente}")

print("Programa terminado.")
