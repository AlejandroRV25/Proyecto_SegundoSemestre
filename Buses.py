

class Buses:
    def __init__(self, placa, color, tarifa, empresa, chofer, parada1, parada2, parada3, parada4, parada5, parada6):
        self.placa = placa
        self.color = color
        self.tarifa = tarifa
        self.empresa = empresa
        self.chofer = chofer
        self.parada1 = parada1
        self.parada2 = parada2
        self.parada3 = parada3
        self.parada4 = parada4
        self.parada5 = parada5
        self.parada6 = parada6

    def getParada1(self):
        return self.parada1

    def getParada2(self):
        return self.parada2

    def getParada3(self):
        return self.parada3

    def getParada4(self):
        return self.parada4

    def getParada5(self):
        return self.parada5

    def getParada6(self):
        return self.parada6

    def getEmpresa(self):
        return self.empresa

    def getChofer(self):
        return self.chofer

    def getPlaca(self):
        return self.placa

    def getColor(self):
        return self.color

    def getTarifa(self):
        return self.tarifa

    def extraerPlaca(self):
        print('{}'.format(self.placa))
    
    def extraerEmpresa(self):
        print('{}'.format(self.empresa))

    def extraerChofer(self):
        print('{}'.format(self.chofer))
    
    def extraerColor(self):
        print('{}'.format(self.color))

    def extraerTarifa(self):
        print('{}'.format(self.tarifa))

    def extraerParada1(self):
        print('{}'.format(self.parada1))

    def extraerParada2(self):
        print('{}'.format(self.parada2))

    def extraerParada3(self):
        print('{}'.format(self.parada3))
    
    def extraerParada4(self):
        print('{}'.format(self.parada4))

    def extraerParada5(self):
        print('{}'.format(self.parada5))

    def extraerParada6(self):
        print('{}'.format(self.parada6))
    
    def organizarFinalParadas(self):
        print('Según sus paradas, el bus más óptimo para usted tiene la matrícula {}, de la empresa {} y de color {}, conducido por {}, con una tarifa de {} pesos, pasará por {}, {}, {}, {}, {} y por último {}'.format(self.placa, self.empresa, self.color, self.chofer, self.tarifa,self.parada1, self.parada2, self.parada3, self.parada4, self.parada5, self.parada6))

    def organizarFinal(self):
        print('El bus con matrícula {}, de la empresa {} y de color {}, conducido por {},  con una tarifa de {} pesos, pasará con destino a {}'.format(self.placa, self.empresa, self.color, self.chofer, self.tarifa, self.parada1))
