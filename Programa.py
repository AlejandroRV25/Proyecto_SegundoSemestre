from collections import Counter
import re
from Buses import Buses 
from Flota import Flota
from Listas import Listas
from Tiempo import Tiempo

lista = Listas()
flota = Flota()

def comparar(a, b):
    return Counter(a)==Counter(b)

def normalizar(txt):
	txt = txt.lower()
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
	for i in acentos:
		if i in txt:
			txt = txt.replace(i, acentos[i])
	return txt

def confirmar(texto):
	while texto not in lista.lista_comparadora:
		texto = input('Por favor asegurese de escribir el nombre de su destino correctamente: ')
		texto = normalizar(texto)
	return texto

def destino():
	print('Destinos posibles:\n\t-Sultana   -Villa Pilar\n\t-Palermo   -La Linda\n\t-Fátima    -Puertas del Sol\n\t-Turín     -San Cayetano\n\t-Carola    -Liborio\n\t-Bengala   -Estadio')
	Buscador = input('Digite su destino: ')
	Buscador = confirmar(normalizar(Buscador)); return Buscador

flota.generacionBuses(Flota.horariosChofer())

verificacion_paradas = int(input('Digite "1" si desea buscar una ruta con más de una parada, de lo contrario digite "0": '))
while 0 != verificacion_paradas != 1:
	verificacion_paradas = int(input('Digite "1" si desea buscar una ruta con más de una parada, de lo contrario digite "0": '))
#Con paradas.
if verificacion_paradas == 1:
	Paradas_Adicionales = int(input('Digite la cantidad de paradas adicionales que desea buscar con un máximo de 5: '))
	while Paradas_Adicionales < 0:
		Paradas_Adicionales = int(input('Digite la cantidad de paradas adicionales que desea buscar con un máximo de 5: '))
	lista_busqueda =[]
	lista_resultados = []
	Posicion = lista.lista_comparadora_paradas.index(normalizar(destino()))
	for paradas in range(Paradas_Adicionales):
		texto = paradas + 1; texto = str(texto); texto = 'Digite la parada número ' + texto + ': '
		parada = input(texto); confirmar(normalizar(parada))
		lista_busqueda.append(parada)
	for ubicacion in range(12):
		lista_temporal = []
		lista_temporal.append(lista.lista_parada_1[ubicacion])
		lista_temporal.append(lista.lista_parada_2[ubicacion])
		lista_temporal.append(lista.lista_parada_3[ubicacion])
		lista_temporal.append(lista.lista_parada_4[ubicacion])
		lista_temporal.append(lista.lista_parada_5[ubicacion])
		lista_temporal.append(lista.lista_parada_6[ubicacion])
		comparador = set(lista_temporal) & set(lista_busqueda); comparador = list(comparador)
		comparacion = comparar(lista_busqueda, comparador)
		if comparacion == True:
			lista_resultados.append(ubicacion)
	if len(lista_resultados) > 0:
		(tiempo, contador_minutos) = Tiempo.calculo(Tiempo.getHour())
		bus = flota.buses[lista_resultados[0]]; bus.organizarFinalParadas(); print('pasará por su ubicación en ', contador_minutos, 'minutos, a las ', tiempo, ' aproximadamente.')
	else:
		print('Lo sentimos, no encontramos un bus que cumpla con sus requisitos.')
#Sin paradas. Terminado.
else:
	(tiempo, contador_minutos) = Tiempo.calculo(Tiempo.getHour())
	Posicion = lista.lista_comparadora.index(destino())
	bus = flota.buses[Posicion]; bus.organizarFinal(); print('en ', contador_minutos, 'minutos, a las ', tiempo, ' aproximadamente.') 
