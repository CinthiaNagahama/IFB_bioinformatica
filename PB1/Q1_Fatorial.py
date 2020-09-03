# -*- coding:utf-8 -*-

def fatorial(n):
	fat = 1
	for i in range(n):
		fat *= n
		n = n - 1
	return fat


n = int(input())

print(fatorial(n))