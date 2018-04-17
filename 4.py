# -*- coding: iso-8859-15 -*-

#Ex. 1 - Simulando o lançamento de um dado de seis lados:
import random

print "Lado do dado:", random.randint(1, 6)

print'\n'

####################################################

#Ex. 2 - Simulando um jogo de adivinhação numérica:
import random 

print "Adivinhe o número sorteado entre 1 e 1000"

numSorteado = random.randint(1, 1000)
palpite = input("Digite seu palpite: ")

while palpite != numSorteado:
	if palpite < numSorteado:
		palpite = input("Dê um palpite que seja maior: ")

	elif palpite > numSorteado:
		palpite = input("Dê um palpite que seja menor: ")

print "Parabéns, você acertou!"

####################################################