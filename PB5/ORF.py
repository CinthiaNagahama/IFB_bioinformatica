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
def create_file(orfs, orders):
	newFileName = "orfs.fasta"
	file = open(newFileName, "w")
	for index, order in enumerate(orders):
		file.write(f">orf {order:+d}\n{orfs[index]}\n")
	file.close()

# Main
fileName = "gene.fasta"
with open(fileName) as fp:
	fpContent = fp.readlines()

	sequence = fpContent[1]
	orders = (1, 2, 3, -1, -2, -3)

	orfs = []
	for order  in orders:
		if(order > 0):
			orfs.append(downstream(sequence, order))
		else:
			orfs.append(upstream(sequence, order))

	create_file(orfs, orders)