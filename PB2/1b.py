# -*- coding:utf-8 -*-
import re


def Traduz(string):
	string = re.sub("A", "U", string)
	string = re.sub("T", "A", string)

	string = re.sub("C", "S", string)
	string = re.sub("G", "C", string)
	string = re.sub("S", "G", string)

	return string


fileName = "toxins_3-5.fna"

fita_molde_re = re.compile("\]([ATCG]+)")

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

	# Cria uma lista de mRNA
	mRNA = []
	for match in fita_molde_re.finditer(fpContent):
		start = match.start()
		end = match.end()
		mRNA.append((Traduz(fpContent[start+1:end]))[::-1])
		
	# Escreve (em) um arquivo o mRNA
	novoArquivo = open("mRNA_toxins.fna", "w")
	for i in range(len(headers)):
		novoArquivo.write(headers[i])
		novoArquivo.write("\n")
		novoArquivo.write(mRNA[i])
		novoArquivo.write("\n")

	novoArquivo.close()