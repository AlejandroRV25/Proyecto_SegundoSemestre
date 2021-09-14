from datetime import datetime
import re

class Tiempo: 
    def getHour():
        TiempoPC = datetime.now().time()
        conversor_tiempo = str(TiempoPC)
        TiempoHorasMinutos = conversor_tiempo[0:5]
        tiempo = re.sub(':','', TiempoHorasMinutos)
        tiempo = int(tiempo)
        return tiempo

    def calculo(tiempo):
        contador_minutos = 0
        operacion = tiempo % 10
        if operacion != 0:
            while operacion != 0:
                contador_minutos = contador_minutos + 1
                tiempo = tiempo + 1
                operacion = tiempo % 10
            tiempo = str(tiempo)
            if len(tiempo) == 3:
                tiempo = '0' + tiempo 
            tiempo_A = tiempo[0:2]; tiempo_B = tiempo[2:4]
            if tiempo_B == '60':
                tiempo_A = int(tiempo_A); tiempo_A = tiempo_A + 1; tiempo_A = str(tiempo_A)
                tiempo_B = '00'   
            tiempo = tiempo_A + ':' + tiempo_B
        else:
            contador_minutos = 10
            tiempo = tiempo + 10
            tiempo = str(tiempo)
            if len(tiempo) == 3:
                tiempo = '0' + tiempo
            tiempo_B = tiempo[2:4]; tiempo_A = tiempo[0:2]
            if tiempo_B == '60':
                tiempo_A = int(tiempo_A); tiempo_A = tiempo_A + 1; tiempo_A = str(tiempo_A)
                tiempo_B = '00'
            tiempo = tiempo_A + ':' + tiempo_B
        return (tiempo, contador_minutos)
