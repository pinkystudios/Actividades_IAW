# Requerir al usuario que ingrese un día de la semana en minusculas
# e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes
# otro mensaje diferente si es sábado o domingo. 
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

def diasemana (dia_semana):

    if dia_semana == "lunes":
        print("¡Ten un buen inicio de semana!")
    elif dia_semana == "viernes":
        print("¡Ya es viernes!")
    elif dia_semana == "sabado" or dia_semana == "domingo":
        print("¡Feliz fin de semana, ten un buen descanso!")
    else:
        print("¡Espero estes teniendo una buena semana!")
        
dia_semana = input ("¿Que dia es hoy?: ")
diasemana (dia_semana)