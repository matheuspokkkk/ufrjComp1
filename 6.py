# -*- coding: iso-8859-15 -*-

#Ex.1 - Contando o número de linhas em um arquivo:
import fileinput

contador = 0
for linha in fileinput.input("palavras.txt"):
	contador += 1

print contador
print

####################################################

#Ex.2 - Imprimindo as linhas com a maior quantidade
#de caracteres em um arquivo: 
import fileinput

tamanhoMax = 0
for linha in fileinput.input("palavras.txt"):
	linha = linha.strip()

	if len(linha) > tamanhoMax:
		tamanhoMax = len(linha)

for linha in fileinput.input("palavras.txt"):
	linha = linha.strip()

	if len(linha) == tamanhoMax:
		print linha

print

####################################################

#Ex.3 - Imprimindo palíndromos presentes no arquivo:
import fileinput

for linha in fileinput.input("palavras.txt"):
	linha = linha.strip()

	if linha == linha[::-1]:
		print linha

print

####################################################

#Ex.4 - Imprimindo as linhas que respeitam um determinado padrão de composição:
import fileinput

padrao = "S**V***R**"

for linha in fileinput.input("palavras.txt"):
	linha = linha.strip()

	if len(linha) == len(padrao) and \
	linha[0] == padrao[0] and \
	linha[3] == padrao[3] and \
	linha[7] == padrao[7]:

		print linha

####################################################

