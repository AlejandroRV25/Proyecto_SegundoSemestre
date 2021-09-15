from Buses import Buses
from Tiempo import Tiempo
from Listas import Listas

lista =Listas()

class Flota:
    buses = []

    def addBus(self, placa, color, tarifa, empresa, chofer, parada1, parada2, parada3, parada4, parada5, parada6):
        bus = Buses(placa, color, tarifa, empresa, chofer, parada1, parada2, parada3, parada4, parada5, parada6)
        self.buses.append(bus)
    
    def horariosChofer():
        if Tiempo.getHour() < 600 or Tiempo.getHour() > 2159:
            print('Usted no se encuentra en el horario de funcionamiento.')
        else:
            if (Tiempo.getHour() >= 600) and (Tiempo.getHour() <= 1000):
                chofer = lista.lista_chofer_6_10
            elif (Tiempo.getHour() > 1000 ) and (Tiempo.getHour() <= 1400):
                chofer = lista.lista_chofer_10_14
            elif (Tiempo.getHour() > 1400) and (Tiempo.getHour() <= 1800):
                chofer = lista.lista_chofer_14_18
            elif (Tiempo.getHour() > 1800) and (Tiempo.getHour() <= 2200):
                chofer = lista.lista_chofer_18_22
        return chofer
    
    def generacionBuses(self, chofer):
        for i in range(12):
            self.addBus(lista.lista_placas[i], lista.lista_colores[i], lista.lista_tarifas[i], lista.lista_empresas[i], chofer[i], lista.lista_parada_1[i], lista.lista_parada_2[i], lista.lista_parada_3[i], lista.lista_parada_4[i], lista.lista_parada_5[i], lista.lista_parada_6[i])
        
    
