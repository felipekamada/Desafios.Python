#!/usr/bin/env python

lista = (input('Digite a lista:'))

def somadenumeros (lista):
	soma = 0
	for i in lista:
		soma = soma + i
	return soma	

print(somadenumeros([]))
