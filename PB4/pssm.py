# -*- coding:utf-8 -*-

import re
import math
from beautifultable import BeautifulTable

# Encontra as frequências parciais
def frequence_table():
	# Encontra o total de bases nitrogenadas
	total = 0
	for occurrence in occurrences:
		total += int(occurrence)

	# Encotra a frequência de cada base nitrogenada por posição
	positions = []
	for pos in range(len(sequences[0])):
		freq_a = 0
		freq_t = 0
		freq_g = 0
		freq_c = 0

		for i in range(len(sequences)):
			if(sequences[i][pos] == 'A'):
				freq_a += int(occurrences[i])

			elif(sequences[i][pos] == 'T'):
				freq_t += int(occurrences[i])
			
			elif(sequences[i][pos] == 'G'):
				freq_g += int(occurrences[i])

			elif(sequences[i][pos] == 'C'):
				freq_c += int(occurrences[i])

		A.append(freq_a / total)
		T.append(freq_t / total)
		G.append(freq_g / total)
		C.append(freq_c / total)

		positions.append(str(pos + 1))

	sum_bases.append(sum(A)/len(positions))
	sum_bases.append(sum(T)/len(positions))
	sum_bases.append(sum(G)/len(positions))
	sum_bases.append(sum(C)/len(positions))

	return positions

# Normaliza
def normalize():
	for i in range(len(A)):
		if(A[i] != '-'):
			A[i] = A[i]/sum_bases[0]
		if(T[i] != '-'):
			T[i] = T[i]/sum_bases[1]
		if(G[i] != '-'):
			G[i] = G[i]/sum_bases[2]
		if(C[i] != '-'):
			C[i] = C[i]/sum_bases[3]

# Converte os scores para escala logarítmica de base 2
def log2():
	for i in range(len(A)):
		if(A[i] != '-'):
			A[i] = math.log2(A[i])
		if(T[i] != '-'):
			T[i] = math.log2(T[i])
		if(G[i] != '-'):
			G[i] = math.log2(G[i])
		if(C[i] != '-'):
			C[i] = math.log2(C[i])

# Substitui o valor 0 por caracteres -
def exchange_zero():
	for i in range(len(A)):
		if(A[i] == 0):
			A[i] = '-'
		if(T[i] == 0):
			T[i] = '-'
		if(C[i] == 0):
			C[i] = '-'
		if(G[i] == 0):
			G[i] = '-'

# Deseha a tabela
def draw_table(columnHeader, row_Header, overallFrequency):
	table = BeautifulTable()

	table.columns.header = columnHeader

	table.rows.append(A, header="A")
	table.rows.append(T, header="T")
	table.rows.append(G, header="G")
	table.rows.append(C, header="C")

	if(overallFrequency):
		table.columns.append(sum_bases, header="Frequência Geral")

	table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
	print(table)

def end_score():
	for i in range(len(sequences)):
		partialScore = 0
		for pos in positions:
			if(sequences[i][int(pos)-1] == 'A'):
				partialScore += A[int(pos)-1]
			elif(sequences[i][int(pos)-1] == 'T'):
				partialScore += T[int(pos)-1]
			elif(sequences[i][int(pos)-1] == 'G'):
				partialScore += G[int(pos)-1]
			elif(sequences[i][int(pos)-1] == 'C'):
				partialScore += C[int(pos)-1]
		score.append(str(partialScore).replace(".", ","))

# Cria o arquivo com os scores
def create_file():
	newFileName = filename + ".scores"
	scores = open(newFileName, "w")
	for i in range(len(sequences)):
		scores.write(sequences[i])
		scores.write("\t")
		scores.write(score[i])
		scores.write("\n")
	scores.close()

# ------------------------------------------ Main ------------------------------------------ #


filename = "C.motif"
line_re = re.compile("([TCGA]+)+\t([0-9]+)")

BASES = ['A', 'T', 'G', 'C']

with open(filename) as fp:
	fpContent = fp.readlines()

	sequences = []
	occurrences = []
	
	# Separa sequências e frequências
	for line in fpContent:
		match = line_re.match(line)
		sequences.append(match.group(1))
		occurrences.append(match.group(2))

	A = []
	T = []
	G = []
	C = []
	sum_bases = []

	print("\t\t\t.------------------------.")
	print("\t\t\t| Construção de uma PSSM |")
	print("\t\t\t'------------------------'")
	
	print("\n-> Passo 1:")
	print("\tPreencher a tabela com as frequências de cada resíduo em cada posição do alinhamento múltiplo")

	positions = frequence_table()
	exchange_zero()

	draw_table(positions, BASES, 1)

	print("\n-> Passo 2:")
	print("\tNormalizar as frequências dividindo as frequências posicionais de cada resíduo pela frequência total")
	
	normalize()

	draw_table(positions, BASES, 1)

	print("\n-> Passo 3:")
	print("\tConverter os scores normalizados para escala logarítmica na base 2")
	print("\t\t- Scores positivos representam um match idêntico ou bastante similar do resíduo com sua posição")
	print("\t\t- Scores negativos representam um match de resíduo não conservado")

	log2();

	draw_table(positions, BASES, 0)

	score = []
	end_score()
	create_file()