# -*- coding: iso-8859-15 -*-

#Ex.1 - Obtendo-se um valor à partir da soma das unidades, dezenas e centenas que o constituem:
def montaNumero(unidades, dezenas, centenas):
	return unidades + dezenas*10.0 + centenas*100.0

print "Somando-se 3 unidades, com 5 dezenas e 1 centena, obtem-se o número", montaNumero(3, 5, 1)
print

####################################################

#Ex.2 - Imprimindo a soma dos dez primeiros termos da sequência 1 - 1/4 + 1/9 - 1/16 + 1/25 ... :
contador = 0
for i in range(1, 11):
	if i % 2 != 0:
		contador += 1.0 / i**2

	else:
		contador -= 1.0 / i**2

print "Soma =", contador
print

####################################################

#Ex.3 - Estimando o valor de pi tendo como parâmetro o número de termos que serão utilizados no cálculo da aproximação:
import math

def calculaPi(numeroDeTermos):
	contador = 0
	for i in range(1, numeroDeTermos+1):
		if i % 2 != 0:
			contador += 1.0 / i**2

		else:
			contador -= 1.0 / i**2

	return math.sqrt(12 * contador)

print "Termos: 10"
print "Valor Calculado:", calculaPi(10)
print

####################################################

#Ex.4 - Estimando o valor de pi usando como quantidade de termos as potências de dez até 10**6,
#e comparando o valor obtido com o de pi da biblioteca math:
import math
import locale

def calculaPi(numeroDeTermos):
	contador = 0
	for i in range(1, numeroDeTermos+1):
		if i % 2 != 0:
			contador += 1.0 / i**2

		else:
			contador -= 1.0 / i**2

	return math.sqrt(12 * contador)

print locale.format('%8s', "Termos"),\
      locale.format('%15s', "Val Calculado"),\
      locale.format('%11s', "Diferenca")

for i in range(0, 7):
	meuPi = calculaPi(10**i)
	print locale.format('%8d', 10**i),\
	      locale.format('%15.8f', meuPi),\
	      locale.format('%11.8f', math.pi - meuPi)

print

####################################################

#Ex.5 - Criando uma função que calcula o MDC entre dois números inteiros:
def calculaMDC(a, b):
	while a != b:
		if a > b:
			a -= b

		else:
			b -= a

	return a

print "O MDC entre 15 e 5 é:", calculaMDC(15, 5)
print 

####################################################

#Ex.6 - Criando uma função que calcula o fatorial de um número inteiro:
def calculaFatorial(x):
	if x == 0:
		return 1

	else:
		resultado = x * calculaFatorial(x - 1)

		return resultado

print "5! =", calculaFatorial(5)
