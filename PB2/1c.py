# -*- coding:utf-8 -*-
import re

'''
IUPAC amino acid code	Three letter code	Amino acid
		A						Ala 		Alanine
		C						Cys			Cysteine
		D						Asp			Aspartic Acid
		E						Glu			Glutamic Acid
		F						Phe			Phenylalanine
		G						Gly			Glycine
		H						His			Histidine
		I						Ile			Isoleucine
		K						Lys			Lysine
		L						Leu			Leucine
		M						Met			Methionine
		N						Asn			Asparagine
		P						Pro			Proline
		Q						Gln			Glutamine
		R						Arg			Arginine
		S						Ser			Serine
		T						Thr			Threonine
		V						Val			Valine
		W						Trp			Tryptophan
		Y						Tyr			Tyrosine
'''

def Transcreve(string):
	IUPAC_codigo_aminoacidos = {
	"A" : ["GCU", "GCC", "GCA", "GCG"],
	"C" : ["UGU", "UGC"],
	"D" : ["GAU", "GAC"],
	"E" : ["GAA", "GAG"],
	"F" : ["UUU", "UUC"],
	"G" : ["GGU", "GGC", "GGA", "GGG"],
	"H" : ["CAU", "CAC"],
	"I" : ["AUU", "AUC", "AUA"],
	"K" : ["AAA", "AAG"],
	"L" : ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
	"M" : ["AUG"],
	"N" : ["AAU", "AAC"],
	"P" : ["CCU", "CCC", "CCA", "CCG"],
	"Q" : ["CAA", "CAG"],
	"R" : ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
	"S" : ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
	"T" : ["ACU", "ACC", "ACA", "ACG"],
	"V" : ["GUU", "GUC", "GUA", "GUG"],
	"W" : ["UGG"],
	"Y" : ["UAU", "UAC"]
	}

	# Identifica o tipo do aminoácido | Para antes de chegar à tripla de parada (UAG, UAA, UGA)
	aminoacido = []
	for i in range(0, len(string)-3, 3):
		for k, v in IUPAC_codigo_aminoacidos.items():
			if (string[i:i+3]) in v:
				code = k

		aminoacido.append(code)


	aminoacido = "".join(aminoacido)

	return aminoacido
	


fileName = "mRNA_toxins.fna"

sequencia_RNA_re = re.compile("\]([AUCG]+)")

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

	# Cria uma lista de aminoácidos

	aminoacidos = []


	for match in sequencia_RNA_re.finditer(fpContent):
		start = match.start()
		end = match.end()
		aminoacidos.append(Transcreve(fpContent[start+1:end]))
	
	# Escreve (em) um arquivo com os aminoácidos
	novoArquivo = open("toxins.faa", "w")
	for i in range(len(headers)):
		novoArquivo.write(headers[i])
		novoArquivo.write("\n")
		novoArquivo.write(aminoacidos[i])
		novoArquivo.write("\n")

	novoArquivo.close()