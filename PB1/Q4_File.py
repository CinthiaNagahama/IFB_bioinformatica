# -*- coding:utf-8 -*-

filename = "sequence.fasta"

with open(filename) as fp:
	header = []
	content = []

	for linha in fp:
		if linha[0] == ">":
			header.append(linha[0:-1])
		else:
			content.append(linha[0:-1])

	fpContent = dict(zip(header, content))

	for key in fpContent:
		print("(" + key + ", " + fpContent[key] + ")")