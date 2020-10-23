# -*- coding:utf-8 -*-
import re

# Encontra ORFs 3'->5'
def downstream(sequence, order):
	if(order == 1):
		return (sequence[order - 1:])
	else:
		return (sequence[order - 1: len(sequence) - (3 - order + 1)])

# Encontra ORFs 5'->3'
def traduz(string):
	string = re.sub("A", "S", string)
	string = re.sub("T", "A", string)
	string = re.sub("S", "T", string)

	string = re.sub("C", "S", string)
	string = re.sub("G", "C", string)
	string = re.sub("S", "G", string)

	return string

def upstream(sequence, order):
	sequence = traduz(sequence)[::-1]
	return downstream(sequence, -order)

# Cria arquivo
def create_file(orfs):
	newFileName = "orfs.fasta"
	file = open(newFileName, "w")
	for i in range(1, 7):
		file.write(">orf +" + str(i))
		file.write("\n")
		file.write(orfs[i - 1])
		file.write("\n")
	file.close()

# Main
fileName = "gene.fasta"
with open(fileName) as fp:
	fpContent = fp.readlines()

	sequence = fpContent[1]

	orfs = []
	for i  in range(1, 4):
		orfs.append(downstream(sequence, i))

	for i  in range(-1, -4, -1):
		orfs.append(upstream(sequence, i))

	create_file(orfs)