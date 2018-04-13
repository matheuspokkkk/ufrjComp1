# -*- coding: iso-8859-15 -*-

#Ex. 1 - Recebendo três números e imprimindo o de maior valor:
pNumero = input("Digite o primeiro número: ")
sNumero = input("Digite o segundo número: ")
tNumero = input("Digite o terceiro número: ")

if pNumero >= sNumero and pNumero >= tNumero:
	print pNumero
elif sNumero >= pNumero and sNumero >= tNumero:
	print sNumero
else:
	print tNumero

print'\n\n'

####################################################

#Ex. 2 - Imprimindo a raiz quadrada dos números inteiros de 2 até 10, seguindo uma formatação específica:
import math
import locale

print "Número", locale.format('%13s', "Raiz Quadrada")

numero = 2
while numero < 11:
	print locale.format('%4d', numero),\
	locale.format('%14.8f', math.sqrt(numero))

	numero += 1

print "Fim da Tabela"

print'\n\n'

####################################################

#Ex. 3 - Imprimindo diferentes sequências numéricas:
#a)1, 2, 3, 4, 5, 6, 7, 8, 9, 10
x = 1
while x < 11:
	print x,
	x += 1

print'\n\n'

#b)1, 4, 9, 16, 25, 36, 49, ... (que não passem de 100.000)
x = 1
while x*x <= 100000:
	print x*x,
	x += 1

print'\n\n'

#c)1, 10, 100, 1000, 10000, ... (que não passem de 10¹⁰)
x = 0
while x < 11:
	print 10**x,
	x += 1

print'\n\n'

#d)1, 2, 4, 8, 16, 32, 64, ... (que não passem de 1G)
x = 1
while x <= 10**9:
	print x,
	x *= 2

print'\n\n'

####################################################

#Ex. 4 - Encontrando o Máximo Divisor Comum (MDC) de dois números inteiros positivos
a, b = raw_input("Entre com dois números inteiros positivos: ").split()
a, b = [int(a), int(b)]

while a != b:
	if a > b:
		a -= b
	else:
		b -= a

print "Máximo divisor: ", a

print'\n\n'

####################################################