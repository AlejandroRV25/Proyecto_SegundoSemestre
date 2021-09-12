from datetime import datetime
import re

class Tiempo: 
    #Lector de la hora del equipo.
    Tiempo = datetime.now().time()
    conversor_tiempo = str(Tiempo)
    tiempo_final = conversor_tiempo[0:5]
    tiempo = re.sub(':','', tiempo_final)
    tiempo = int(tiempo)

    #Calculo de la hora.
    cont = 0
    if tiempo < 600 or tiempo > 2200:
        print('usted no se encuentra en el horario de funcionamiento.')
    else:
        operacion = tiempo % 10
        if operacion != 0:
            while operacion != 0:
                cont = cont + 1
                tiempo = tiempo + 1
                operacion = tiempo % 10
            tiempo = str(tiempo); A = tiempo[0:2]; B = tiempo[2:4]; tiempo = A + ':' + B
            print('en ', cont,' minutos, un bus pasará por su ubicación. Hora aproximada:', tiempo)
        elif operacion == 0:
            tiempo = tiempo + 10; tiempo = str(tiempo); A = tiempo[0:2]; B = tiempo[2:4]; tiempo = A + ':' + B
            print('El bus está apunto de pasar o ya pasó, el siguiente bus pasará en 10 minutos. Hora aproximada: ', tiempo)