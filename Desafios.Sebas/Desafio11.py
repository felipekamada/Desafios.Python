import Desafio6
def ordenamaior (lista):
	copialista = [x for x in lista]
	listaordenadamaior = []
	for i in range(len(copialista)):
		listaordenadamaior.insert(0,Desafio6.retirarmenor(copialista))
	return listaordenadamaior
