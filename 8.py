# -*- coding: iso-8859-15 -*-

#Ex.1 - Criando um programa que fornece o número de vezes que cada valor possível foi sorteado na Mega Sena:
import fileinput
import locale

print locale.format('%8s', "Dezenas"),\
      locale.format('%8s', "Ocorrências")

for i in range(1, 61):
	numeroOcorrencias = 0

	for linha in fileinput.input("resultadosMegaSena.txt"):
		linha = linha.strip()
		linha = linha.split()
		linha = [int(numero) for numero in linha]

		if i in linha[1:]:
			numeroOcorrencias += 1

	if i < 10:	
		print locale.format('%6s', '0' + str(i)),\
		      locale.format('%6d', numeroOcorrencias)
	else:
		print locale.format('%6d', i),\
		      locale.format('%6d', numeroOcorrencias)

print

####################################################

#Ex.2 - Criando uma função que cria um arquivo .csv com o número de vezes que cada valor possível foi sorteado na MegaSena:
import fileinput
import locale

def gravaNoArquivo():
	arquivo = open("outputMegaSena.csv", 'w')
	arquivo.write("Dezenas,Ocorrências\n")

	for i in range(1, 61):
		numeroOcorrencias = 0

		for linha in fileinput.input("resultadosMegaSena.txt"):
			linha = linha.strip()
			linha = linha.split()
			linha = [int(numero) for numero in linha]

			if i in linha[1:]:
				numeroOcorrencias += 1

		if i < 10:	
			arquivo.write('0' + str(i) + ',' + str(numeroOcorrencias) + '\n')

		else:
			arquivo.write(str(i) + ',' + str(numeroOcorrencias) + '\n')

	return arquivo

	arquivo.close()

gravaNoArquivo()