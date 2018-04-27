def somamenor (listas):
	menor = None
	for lista in listas:
		soma = 0
		for x in lista:
			soma = soma + x
		if (menor is None):
			menor = soma
		elif (soma < menor):

			menor = soma				
	return menor
