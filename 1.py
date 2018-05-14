# -*- coding: iso-8859-15 -*-

#Ex. 1 - Saudando o mundo:
print "Hello World!"

print

####################################################

#Ex. 2 - Calculando a média da disciplina Computação 1:
notaP1 = input("Digite a nota da primeira prova: ")
notaP2 = input("Digite a nota da segunda prova: ")
mediaTrabalhos = input("Digite a média dos trabalhos: ")

if notaP1 == 'N' or notaP2 == 'N':
	print "Segunda Chamada"

else:
	mediaTotal = ((notaP1 + notaP2) / 2.0) * 0.8 + mediaTrabalhos * 0.2

	print "Notas:", notaP1, notaP2, mediaTrabalhos
	print "Média:", mediaTotal

	if mediaTotal >= 7.0:
		print "Aprovado"
	elif mediaTotal < 3.0:
		print "Reprovado"
	else:
		print "Prova Final"
		
print

####################################################

#Ex. 3 - Encontrando as raízes reais de uma equação:
import math

a, b, c = input("Entre com os coeficientes a, b e c: ")

delta = b * b - 4.0 * a * c	

if delta < 0:
	print "A equação não possui raízes reais"

elif delta == 0:
	x = (b * (-1.0) + math.sqrt(delta)) / (2.0 * a)

	print "A única raíz é: ", x

else:
	x1 = (b * (-1.0) + math.sqrt(delta)) / (2.0 * a)
	x2 = (b * (-1.0) - math.sqrt(delta)) / (2.0 * a)

	print "As raízes são:", x1, x2

####################################################




