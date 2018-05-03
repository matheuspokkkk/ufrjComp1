# -*- coding: iso-8859-15 -*-

#Ex.1 - Imprimindo as tabuadas de 3 à 20 utilizando o comando for:
for x in range(3, 21, 1):
	for y in range(1, 21, 1):
		print x, 'x', y, '=', x * y 

print'\n'

####################################################

#Ex. 2 - Encontrando os Números de Armstrong de 0 à 999 utilizando o comando for:
for centenas in range(0, 10, 1):
	for dezenas in range(0, 10, 1):
		for unidades in range(0, 10, 1):
			numeroCandidato = centenas * 100 + dezenas * 10 + unidades

			if numeroCandidato == centenas**3 + dezenas**3 + unidades**3:
				print numeroCandidato

print'\n'

####################################################

#Ex. 3 - Gerando as datas válidas de 01/01/2001 até 31/12/2004, utlizando o comando for e considerando como
#        bissextos os anos múltiplos de 4:
for ano in range(2001, 2005, 1):	
	for mes in range(1, 13, 1):
		if mes == 2:
			if ano % 4 == 0:
				quantidadeDias = 29
				
			else:
				quantidadeDias = 28

		elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
			quantidadeDias = 30

		else:
			quantidadeDias = 31

		for dia in range(1, quantidadeDias + 1, 1):
			print dia, '/', mes, '/', ano

####################################################