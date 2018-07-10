#Escreva uma função que recebe um número inteiro e retorne True se esse número for divisível por
#2, por 3 e por 5, ou False, se não for divisível por um ou mais desses números.
def ehDivisivelPor2e3e5(numeroCandidatoADivisor):
	if numeroCandidatoADivisor % 2 == 0 and numeroCandidatoADivisor % 3 == 0 and numeroCandidatoADivisor % 5 == 0:
		return True
	else:
		return False

###################################################

#Escreva uma função denominada EHPRIMO que recebe como parâmetro um número inteiro e retorna
#True se esse número é primo ou False, se não.
def EHPRIMO(numeroCandidatoAPrimo):
	denominador = numeroCandidatoAPrimo
	contadorDeDivisoesSemResto = 0

	while denominador > 0:
		if numeroCandidatoAPrimo % denominador == 0:
			contadorDeDivisoesSemResto += 1

		denominador -= 1

	if contadorDeDivisoesSemResto == 2:
		return True
	else:
		return False

###################################################

#Escreva uma função, denominada XPTO, que receba uma string como parâmetro e retorne uma
#string que contém os caracteres que aparecem nessa string, porém sem repetições.
#Por exemplo XPTO(“PARALELO”) retorna “PARLEO".
def XPTO(string):
	caracteresUnicos = ""

	for caractere in string:
		if caractere not in caracteresUnicos:
			caracteresUnicos += caractere

	return caracteresUnicos

###################################################

#Escreva uma função intitulada PALINDROMO que receba uma lista de palavras e retorne uma lista com
#todos os palíndromos da lista recebida.
def PALINDROMO(listaDePalavras):
	listaDePalindromos = []

	for palavra in listaDePalavras:
		palavra = palavra.strip()

		if palavra == palavra[::-1]:
			listaDePalindromos.append(palavra)

	return listaDePalindromos

###################################################

#Escreva uma função denominada SORTEIO que recebe como parâmetro o nome de um arquivo de texto contendo
#uma coleção de palavras, uma em cada linha, e retorne uma das palavras aleatoriamente escolhida.
def SORTEIO(arquivoDeTexto): 
	import random

	arquivo = open(arquivoDeTexto).readlines()

	linhaEscolhida = random.randint(0, len(arquivo) - 1)

	arquivo[linhaEscolhida] = arquivo[linhaEscolhida].strip()

	return arquivo[linhaEscolhida]

###################################################

#Escreva uma função denominada UNIAO que recebe como parâmetros duas listas de palavras, que podem conter
#repetições, e retorne uma lista com o conjunto (sem repetição) união das duas listas.
def UNIAO(listaDePalavras1, listaDePalavras2):
	listaDePalavras3 = []

	for palavra in listaDePalavras1:
		if palavra not in listaDePalavras3:
			listaDePalavras3.append(palavra)

	for palavra in listaDePalavras2:
		if palavra not in listaDePalavras3:
			listaDePalavras3.append(palavra)

	return listaDePalavras3

###################################################

#Escreva uma função denominada INTERSECAO que recebe como parâmetros duas listas de palavras, que podem
#conter repetições, e retorne uma lista com o conjunto (sem repetição) interseção das duas listas.
def INTERSECAO(listaDePalavras1, listaDePalavras2):
	listaDePalavras3 = []

	for palavra in listaDePalavras1:
		if palavra in listaDePalavras2 and palavra not in listaDePalavras3:
			listaDePalavras3.append(palavra)

	return listaDePalavras3

###################################################

#Escreva uma função denominada DIFERENCA que recebe como parâmetros duas listas de palavras, que podem
#conter repetições, e retorne uma lista com o a diferença entre a primeira lista e a segunda.
def DIFERENCA(listaDePalavras1, listaDePalavras2):
	listaDePalavras3 = []

	for palavra in listaDePalavras1:
		if palavra not in listaDePalavras2:
			listaDePalavras3.append(palavra)

	for palavra in listaDePalavras2:
		if palavra not in listaDePalavras1:
			listaDePalavras3.append(palavra)

	return listaDePalavras3

###################################################

#Escreva uma função denominada DOISARQUIVOS que recebe como parâmetros dois nomes de arquivos texto, cada um
#contendo uma coleção de palavras, uma em cada linha, que podem conter repetições, e grave um novo
#arquivo, denominado INTERSECAO, contendo o conjunto (sem repetição) interseção das palavras dos dois arquivos.
def DOISARQUIVOS(arquivoDeTexto1, arquivoDeTexto2):
	arquivo1 = open(arquivoDeTexto1).readlines()
	arquivo2 = open(arquivoDeTexto2).readlines()
	listaIntersecao = []

	for palavra in arquivo1:
		palavra = palavra.strip()

	for palavra in arquivo2:
		palavra = palavra.strip()

	for palavra in arquivo1:
		if palavra in arquivo2 and palavra not in listaIntersecao:
			listaIntersecao.append(palavra)

	arquivoIntersecao = open("INTERSECAO", 'w')

	for palavra in listaIntersecao:
		arquivoIntersecao.write(palavra)

###################################################

#Escreva uma função denominada AVALIA que recebe como parâmetros uma string de gabaritos e uma string de
#respostas de uma prova de múltipla escolha, e retorne o número de respostas certas de acordo com esse gabarito.
#Considere que possa haver eventuais respostas em branco.
#Se houver algum erro nos parâmetros, a função deve retornar -1.
def AVALIA(stringGabaritos, stringRespostas):
	respostasCertas = 0

	if stringGabaritos and stringRespostas and len(stringGabaritos) == len(stringRespostas):
		for questao in range(len(stringGabaritos)):
			if stringGabaritos[questao] == stringRespostas[questao]:
				respostasCertas += 1
	else:
		respostasCertas = -1
	
	return respostasCertas
