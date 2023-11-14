# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
# por pantalla la misma fecha en formato dd de <mes> de aaaa donde 
# <mes> es el nombre del mes

# Creamos el diccionario
dic_meses = {'1': 'Enero', '2':'Febrero', '3': 'Marzo', '4': 'Abril' ,
             '5': 'Mayo', '6':'Junio', '7': 'Julio', '8': 'Agosto' ,
             '9': 'Septiembre', '10':'Octubre', '11': 'Noviembre', '12': 'Diciembre'}

# Recogemos los datos del usuario
fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
dia, mes, año = fecha.split('/') # Separamos en tres campos la respuesta

# Obtenemos el mes en texto y lo imprimimos todo por pantalla
mes_txt = dic_meses[mes]
print(f"La fecha introducida es {dia} de {mes_txt} del año {año}")