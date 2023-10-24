# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario
# introducirá las palabras en español e inglés separadas por dos puntos, y cada
# par <palabra>:<traducción> separados por comas. El programa debe crear un
# diccionario con las palabras y sus traducciones. Después pedirá una frase en español y
# utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el
# diccionario debe dejarla sin traducir.

# Solicitar palabras y traducciones al usuario
entrada = input('Introduce las palabras y sus traducciones \n' +
                'usa el formato "palabra:traducción", separando por comas): ')

# Dividimos la entrada en pares
pares = [par.split(":") for par in entrada.split(",")]

# Creamos el diccionario con las traducciones
traducciones = {par[0]: par[1] for par in pares}

# Solicitamos una frase en español
frase_espanol = input("Introduce una frase en español: ")

# Traducir la frase palabra por palabra
palabras = frase_espanol.split()
frase_traducida = " ".join(traducciones.get(palabra, palabra) for palabra in palabras)

# Mostramos la frase traducida
print(f"Frase traducida: {frase_traducida}")