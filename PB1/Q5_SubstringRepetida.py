# -*- coding:utf-8 -*-

filename = "sequence.fasta"

with open(filename) as fp:
	header = []
	content = []
	maior_valor = []
	maior_repeticao = []

	# Separa as linhas do arquivo em duas listas
	for linha in fp:
		if linha[0] == ">":
			header.append(linha[0:-2])
		else:
			content.append(linha[0:-2])

	# Conta as substrings
	for i in range(len(content)):
		substring = {}
		for j in range(len(content[i]) - 2):
			s = content[i][j : j + 3]
			if (s in substring):
				substring[s] += 1
			else:
				substring[s] = 1

		# Encontra a primeira substring mais repetida
		mValor = substring[list(substring)[0]]
		mRepeticao = list(substring)[0]
		count = 0
		for k in substring: # k -> chave, substring[k] -> valor da chave
			if(mValor < substring[k]):
				mValor = substring[k]
				mRepeticao = list(substring)[count]
			count += 1

		maior_valor.append(mValor)
		maior_repeticao.append(mRepeticao)

	# Transforma as lista em um dicionário
	fpContent = dict(zip(header, content))
	

	# Cria/Adiciona ao arquivo results.txt
	Resultado = open("results.txt", "w")

	count = 0
	for header in fpContent:
		Resultado.write(header)
		Resultado.write(" ")
		Resultado.write(maior_repeticao[count])
		Resultado.write(" ")
		Resultado.write(str(maior_valor[count]))
		Resultado.write("\n")
		
		count += 1

	Resultado.close()