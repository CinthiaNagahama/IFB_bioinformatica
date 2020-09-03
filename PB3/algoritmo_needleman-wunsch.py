# -*- coding:utf-8 -*-

import re
from prettytable import PrettyTable


def cria_matriz_score():
	matriz = []
	for i in range(m):
		linha = []
		for j in range(n):
			linha.append(0)
		matriz.append(linha)
	return matriz


def preenche_matriz_score(matriz):
	# 	Linha 0
	for column in range(1, n):
		matriz[0][column] = matriz[0][column - 1] + scoreGap # Seta Horizontal

	# 	Coluna 0
	for line in range(1, m):
		matriz[line][0] = matriz[line - 1][0] + scoreGap # Seta Vertical

	# 	Resto
	for line in range(1, m):
		for column in range(1, n):

			match = (scoreMatch if v[line - 1] == w[column - 1] else scoreMismatch)

			matriz[line][column] = max(
				matriz[line - 1][column] + scoreGap, # Seta Vertical
				matriz[line][column - 1] + scoreGap, # Seta Horizontal
				matriz[line -1][column -1] + match # Seta Diagonal
				)


def encontra_alinhamento(matriz):
	alignmentA = []
	alignmentB = []

	line = m - 1
	column = n - 1
	
	# Busca a direção da seta
	while(line > 0):
		while(column > 0):
			match = (scoreMatch if v[line - 1] == w[column - 1] else scoreMismatch)

			vet = matriz[line - 1][column] + scoreGap # Seta Vertical
			hor = matriz[line][column - 1] + scoreGap # Seta Horizontal
			dig = matriz[line -1][column -1] + match # Seta Diagonal

			if(matriz[line][column] == vet):
				alignmentA.append(v[line - 1])
				alignmentB.append('-')
				line -= 1
				break

			elif(matriz[line][column] == hor):
				alignmentA.append('-')
				alignmentB.append(w[column - 1])

				column -= 1
				break

			else:
				alignmentA.append(v[line - 1])
				alignmentB.append(w[column - 1])

				line -= 1
				column -= 1
				break

	print("\n\tAlinhamento ótimo:")
	print("\t\t","	".join(alignmentA)[::-1])
	print("\t\t","	".join(alignmentB)[::-1])


def desenha_tabela(matriz):
	table = PrettyTable()

	fields = [" ", "w"]
	for b in w:
		fields.append(b)
	table.add_row(fields)

	column0 = ["v"]
	for a in v:
		column0.append(a)

	for row in range(len(matriz)):
		temp = [column0[row]]
		for i in range(len(matriz[row])):
			temp.append(matriz[row][i])
		table.add_row(temp)

	table.padding_width = 1
	table.junction_char = '+'
	table.align = 'r'
	table.header = False
	print(table)
	table.clear_rows()

	

filename = "sequence.fasta"

dna_re = re.compile("^([ATGC]+)\n?")

with open(filename) as fp:
	# Pega as sequências
	fpContent = fp.readlines()
	v = ""
	w = ""

	for line in fpContent:
		if(not (line[0] == '>') and v != ""):
			w = line.strip("\n")
		if(not (line[0] == '>') and v == ""):
			v = line.strip("\n")

	# Cria a matriz de scores
	m = len(v) + 1 # linhas
	n = len(w) + 1 # colunas

	S = cria_matriz_score()

	# Score
	scoreMatch = 1
	scoreMismatch = -1
	scoreGap = -2

	# Preenche matriz de scores
	preenche_matriz_score(S)

	# Desenha a matriz
	desenha_tabela(S)

	# Escreve as sequência alinhadas
	encontra_alinhamento(S)