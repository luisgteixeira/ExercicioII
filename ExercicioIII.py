import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
	global min_U, max_U, universo_discurso, titulo

	# Valor minimo e maximo do universo de discurso
	min_U = 0.0
	max_U = 50.0

	# # Valor minimo e maximo dos conjuntos
	# min_A = 1.0
	# max_A = 3.0
	# min_B = 2.0
	# max_B = 4.0

	# Cria valor de incremento de acordo com o total de pontos da discretizacao
	pontos = 1000
	discretizacao = (max_U - min_U) / pontos

	# Cria lista com 1000 pontos de discretizacao no intervalo do universo de discurso
	universo_discurso = np.arange(min_U, max_U + discretizacao, discretizacao)

	# Cria matriz com o grau de pertinencia, para cada conjunto Fuzzy, de cada valor do Universo de Discurso
	grau_pertinencia = [[],[],[],[],[]]
	for x in universo_discurso:
		grau_pertinencia[0].append(pertinencia_A(x))
		grau_pertinencia[1].append(pertinencia_B(x))
		grau_pertinencia[2].append(pertinencia_C(x))
		grau_pertinencia[3].append(pertinencia_D(x))
		grau_pertinencia[4].append(pertinencia_E(x))

	
	while (True):

		# opcao = raw_input('Digite letra do exercicio a ser executada (B ou C): ')
		# opcao = opcao.upper()
		opcao = 'C'

		if opcao == 'B':
			# Letra B ------------------ #
			print '----: LETRA B :----\n'
			titulo = 'Conjuntos Fuzzy'
			desenha_grafico(grau_pertinencia)
			# -------------------------- #

		elif opcao == 'C':
			# Letra B ------------------ #
			print '----: LETRA C :----\n'
			valor = input('Digite um valor para Temperatura:')
			novo_grau_pertinencia = pertence_conjunto(grau_pertinencia, valor)
			# -------------------------- #
		elif opcao == 'SAIR':
			print 'Finalizando execucao...'
			break
		else:
			print 'Comando nao encontrado! Digite novamente'


def pertinencia_A(valor):
	if valor < 5:
		return 1
	elif valor >= 5 and valor < 15:
		return (15 - valor) / 10
	else:
		return 0


def pertinencia_B(valor):
	if valor < 5:
		return 0
	elif valor >= 5 and valor < 15:
		return (valor - 5) / 10
	elif valor >= 15 and valor <= 25:
		return (25 - valor) / 10
	else:
		return 0


def pertinencia_C(valor):
	if valor < 15:
		return 0
	elif valor >= 15 and valor < 25:
		return (valor - 15) / 10
	elif valor >= 25 and valor <= 35:
		return (35 - valor) / 10
	else:
		return 0


def pertinencia_D(valor):
	if valor < 25:
		return 0
	elif valor >= 25 and valor < 35:
		return (valor - 25) / 10
	elif valor >= 35 and valor <= 45:
		return (45 - valor) / 10
	else:
		return 0


def pertinencia_E(valor):
	if valor >= 45:
		return 1
	elif valor >= 35 and valor < 45:
		return (valor - 35) / 10
	else:
		return 0


def pertence_conjunto(grau_pertinencia, valor):
	""
	for i,funcao in enumerate(grau_pertinencia):
		for i,funcao in enumerate(grau_pertinencia):
		print universo_discurso[i]

		# if min_U <= valor and max_U >= valor:
		# 	if conjunto[0] <= valor and conjunto[1] >= valor:
		# 		print 'Valor pertence ao Conjunto [', conjunto[0], ',', conjunto[1], ']'
		# 	else:
		# 		print 'Valor nao pertence ao Conjunto [', conjunto[0], ',', conjunto[1], ']'
		# else:
		# 	print 'Valor nao pertence ao Universo de Discurso!'


def desenha_grafico(grau_pertinencia):
	legenda = []
	for i,funcao in enumerate(grau_pertinencia):
		if i == 0:
			cor = 'red'
			label = 'F_A -> Muito Baixa'
		elif i == 1:
			cor = 'green'
			label = 'F_B -> Baixa'
		elif i == 2:
			cor = 'blue'
			label = 'F_C -> Media'
		elif i == 3:
			cor = 'orange'
			label = 'F_D -> Alta'
		elif i == 4:
			cor = 'black'
			label = 'F_E -> Muito Alta'

		plt.plot(universo_discurso, funcao, color=cor)
		legenda.append(mpatches.Patch(color=cor, label=label))
	
	plt.legend(handles=legenda)

	plt.xticks(np.arange(min_U, max_U+2, 1.0))
	plt.yticks(np.arange(0, 2.5, 1))

	axes = plt.gca()
	axes.set_title(titulo)
	axes.set_xlabel('Temperatura')
	axes.set_ylabel('Grau de pertinencia')

	plt.show()


if __name__ == '__main__':
    main()