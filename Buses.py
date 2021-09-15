
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

    def organizarFinalParadas(self):
        print('Según sus paradas, el bus más óptimo para usted tiene la matrícula {}, de la empresa {} y de color {}, conducido por {}, con una tarifa de {} pesos, pasará por: {}, {}, {}, {}, {} y por último {}'.format(self.placa, self.empresa, self.color, self.chofer, self.tarifa,self.parada1, self.parada2, self.parada3, self.parada4, self.parada5, self.parada6))

    def organizarFinal(self):
        print('El bus con matrícula {}, de la empresa {} y de color {}, conducido por {},  con una tarifa de {} pesos, pasará con destino a {}'.format(self.placa, self.empresa, self.color, self.chofer, self.tarifa, self.parada1))
