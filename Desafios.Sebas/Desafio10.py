import Desafio9
def ordenamaior (lista):
	copialista = [x for x in lista]
	listaordenadamaior = []
	for i in range (len(copialista)):
		listaordenadamaior.append(Desafio9.retirarmaior(copialista))
	return listaordenadamaior
