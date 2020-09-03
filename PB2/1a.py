# -*- coding:utf-8 -*-
import re


def Substitui(string):
	string = re.sub("A", "S", string)
	string = re.sub("T", "A", string)
	string = re.sub("S", "T", string)

	string = re.sub("C", "S", string)
	string = re.sub("G", "C", string)
	string = re.sub("S", "G", string)

	return string


fileName = "toxinsNCBI.fna"

fita_codificadora_re = re.compile("\]([ATCG]+)")

with open(fileName) as fp:
	fpContent = fp.readlines()

	# Cria uma lista com os headers
	headers = []
	for line in fpContent:
		if(line[0] == ">"):
			headers.append(line[:-1])

	# Tranforma o conteúdo do arquivo em uma string
	fpContent = "".join(fpContent)
	fpContent = re.split("\n", fpContent)
	fpContent = "".join(fpContent)

	# Cria uma lista de fitas molde
	fita_molde = []
	for match in fita_codificadora_re.finditer(fpContent):
		start = match.start()
		end = match.end()
		fita_molde.append((Substitui(fpContent[start+1:end]))[::-1])
		
	# Escreve (em) um arquivo com fita molde
	novoArquivo = open("toxins_3-5.fna", "w")
	for i in range(len(headers)):
		novoArquivo.write(headers[i])
		novoArquivo.write("\n")
		novoArquivo.write(fita_molde[i])
		novoArquivo.write("\n")

	novoArquivo.close()