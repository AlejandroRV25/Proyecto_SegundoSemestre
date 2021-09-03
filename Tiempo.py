from datetime import datetime
import re

class Tiempo: 
    #Lector de la hora del equipo.
    Tiempo = datetime.now().time()
    conversor_tiempo = str(Tiempo)
    tiempo_final = conversor_tiempo[0:5]
    tiempo = re.sub(':','', tiempo_final)
    tiempo = int(tiempo)

    #Lista horas.
    contador = 1
    llegadaBus = None
    Base = 600
    horas = []
    horas.append('06:00')
    for i in range(1, 961):
        contador = contador + 1
        Hora = Base + i
        if contador == 60:
            Base = Base + 40
            contador = 0
        conversorStr = str(Hora)
        A = conversorStr[0:2]; B = conversorStr[2:4]; horastr = A + ':' + B
        horas.append(horastr)

    #Calculo de la hora.
    cont = 0
    if tiempo < 600 or tiempo > 2200:
        print('usted no se encuentra en el horario de funcionamiento.')
    else:
        for j in horas:
            if tiempo_final == j:
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