# -*- coding: iso-8859-15 -*-

#Ex.1 - Imprimindo as tabuadas de 3 à 20 utilizando o comando for:
for x in range(3, 21, 1):
	for y in range(1, 21, 1):
		print x, 'x', y, '=', x * y 

print

####################################################

#Ex.1.1 - Imprimindo as tabuadas de 3 à 20 utilizando o comando while:
x = 3
while x < 21:
	
	y = 1
	while y < 21:
		print x, 'x', y, '=', x * y 

		y += 1

	x += 1

print

####################################################

#Ex.2 - Encontrando os Números de Armstrong de 0 à 999 utilizando o comando for:
for centenas in range(0, 10, 1):
	for dezenas in range(0, 10, 1):
		for unidades in range(0, 10, 1):
			numeroCandidato = centenas * 100 + dezenas * 10 + unidades

			if numeroCandidato == centenas**3 + dezenas**3 + unidades**3:
				print numeroCandidato

print

####################################################

#Ex.2.1 - Encontrando os Números de Armstrong de 0 à 999 utilizando o comando while:

centenas = 0
while centenas < 10:
	dezenas = 0

	while dezenas < 10:
		unidades = 0

		while unidades < 10:
			numero = unidades + dezenas * 10 + centenas * 100

			if numero == unidades**3 + dezenas**3 + centenas**3:
				print numero

			unidades += 1

		dezenas += 1

	centenas += 1

print

####################################################

#Ex.3 - Gerando as datas válidas de 01/01/2001 até 31/12/2004, utlizando o comando for e considerando como
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

print

####################################################

#Ex.3.1 - Calculando quantos dias já vivi:
contador = 0

for ano in range(1996, 2019, 1):
	if ano == 2018:
		for mes in range(1, 5, 1):
			if mes == 2:
				if ano % 4 == 0:
					quantidadeDias = 29
				
				else:
					quantidadeDias = 28

			elif mes == 4:
				quantidadeDias = 26

			else:
				quantidadeDias = 31

			for dia in range(1, quantidadeDias + 1, 1):
				contador += 1

	else:
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
				contador += 1

print contador
