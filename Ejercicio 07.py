# Escribir un programa que cree un diccionario simulando una cesta de la compra. El
# programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que
# el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y
# el coste total, con el siguiente formato

# Creamos el diccionario del carrito de compras
carrito = {}

# Creamos el bucle para añadir elementos al carrito
while True:
    articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
    
    # Si el usuario escribe 'fin', se acaba el bucle
    if articulo == 'fin':
        break
    
    precio = float(input("Ingrese el precio del artículo: "))
    carrito[articulo] = precio  # El artículo y su valor se añaden al carrito

# Imprimimos el carrito por pantalla
print("\nCarrito de compras:")
for articulo, precio in carrito.items():
    print(f"{articulo} > {precio}€")

# Calculamos el coste total de la compra
total = sum(carrito.values())
print(f"\nCoste total > {total}€")