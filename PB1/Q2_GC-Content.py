# -*- coding:utf-8 -*-

seq = input("Insira uma sequência de DNA: ")

A = 0
C = 0
T = 0
G = 0

for i in seq:
	if i == "A" or i == "a":
		A = A + 1
	elif i == "C" or i == "c":
		C = C + 1
	elif i == "T" or i == "t":
		T = T + 1
	elif i == "G" or i == "g":
		G = G + 1

GC = (G + C)/(A + C + T + G)*100

print(str(round(GC, 1)) + "%")