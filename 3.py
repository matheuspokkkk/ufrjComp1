# -*- coding: iso-8859-15 -*-

#Ex. 1 - Desenhando uma linha reta usando o caracter '+':
print 12 * '+'

print'\n\n'

####################################################

#Ex. 2 - Desenhando um retângulo usando o caracter '+':
contador = 1

while contador < 16:
	print 12 * '+'
	contador += 1

print'\n\n'

####################################################

#Ex. 3 - Desenhando uma diagonal usando o caracter '+':
contador = 0

while contador < 12:
	print contador * ' ' + '+'
	contador += 1

print'\n\n'

####################################################

#Ex. 4 - Desenhando um triângulo usando o caracter '+':
contador = 1

while contador < 13:
	print contador * '+'
	contador += 1

print'\n\n'

####################################################

#Ex. 5 - Desenhando um triângulo invertido usando o caracter '+':
contador = 13

while contador > 0:
	print (13 - contador) * ' ' + contador * '+'
	contador -= 1

print'\n\n'

####################################################

#Ex. 6 - Desenhando uma árvore de natal usando o caracter '+':
contador = 1

while contador < 11:
	print (10 - contador) * ' ' + 2* (contador - 1) * '+'
	contador += 1


####################################################