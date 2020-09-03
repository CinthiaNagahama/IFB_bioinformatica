# -*- coding:utf-8 -*-

seq = input("Insira uma sequência: ")

substrings = {}

for i in range(len(seq) - 3):
	s = seq[i : i + 4]
	if (s in substrings):
		substrings[s] += 1
	else:
		substrings[s] = 1

for key in substrings:
	print(key)