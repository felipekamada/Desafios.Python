import Desafio6
def ordenarmenor (lista):
	copialista = [x for x in lista]
	listaordenada = []
	for i in range(len(copialista)):
		listaordenada.append(Desafio6.retirarmenor(copialista))
	return listaordenada
