def tuplasomalista (listas):
	resultado = []
	for lista in listas:
		soma = 0
		for x in lista:
			soma += x
		tuplelista = (soma, lista)
		resultado.append(tuplelista)
	resultado2 = []
	menor = None
	for x in resultado:
		
