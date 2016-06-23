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

		opcao = raw_input('Digite letra do exercicio a ser executada (B ou C): ')
		opcao = opcao.upper()

		if opcao == 'B':
			# Letra B ------------------ #
			print '----: LETRA B :----\n'
			titulo = 'Conjuntos Fuzzy'
			desenha_grafico(grau_pertinencia)
			# -------------------------- #

		elif opcao == 'C':
			# Letra B ------------------ #
			print '----: LETRA C :----\n'
			valor = input('Digite um valor para Temperatura: ')
			if valor < min_U or valor > max_U:
				print 'Valor nao pertencente ao Universo de Discurso'
				continue
			titulo = 'Conjuntos Fuzzy ativos para Temperatura = ' + str(valor)
			novo_grau_pertinencia = pertence_conjunto(grau_pertinencia, valor)
			desenha_grafico(novo_grau_pertinencia)
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
		return (15.0 - valor) / 10.0
	else:
		return 0


def pertinencia_B(valor):
	if valor < 5:
		return 0
	elif valor >= 5 and valor < 15:
		return (valor - 5.0) / 10.0
	elif valor >= 15 and valor <= 25:
		return (25.0 - valor) / 10.0
	else:
		return 0


def pertinencia_C(valor):
	if valor < 15:
		return 0
	elif valor >= 15 and valor < 25:
		return (valor - 15.0) / 10.0
	elif valor >= 25 and valor <= 35:
		return (35.0 - valor) / 10.0
	else:
		return 0


def pertinencia_D(valor):
	if valor < 25:
		return 0
	elif valor >= 25 and valor < 35:
		return (valor - 25.0) / 10.0
	elif valor >= 35 and valor <= 45:
		return (45.0 - valor) / 10.0
	else:
		return 0


def pertinencia_E(valor):
	if valor >= 45:
		return 1
	elif valor >= 35 and valor < 45:
		return (valor - 35.0) / 10.0
	else:
		return 0


def pertence_conjunto(grau_pertinencia, valor):
	""
	novo_grau_pertinencia = []

	a = pertinencia_A(valor)
	b = pertinencia_B(valor)
	c = pertinencia_C(valor)
	d = pertinencia_D(valor)
	e = pertinencia_E(valor)

	if a == 0:
		novo_grau_pertinencia.append([])
	else:
		novo_grau_pertinencia.append(grau_pertinencia[0])

	if b == 0:
		novo_grau_pertinencia.append([])
	else:
		novo_grau_pertinencia.append(grau_pertinencia[1])

	if c == 0:
		novo_grau_pertinencia.append([])
	else:
		novo_grau_pertinencia.append(grau_pertinencia[2])

	if d == 0:
		novo_grau_pertinencia.append([])
	else:
		novo_grau_pertinencia.append(grau_pertinencia[3])

	if e == 0:
		novo_grau_pertinencia.append([])
	else:
		novo_grau_pertinencia.append(grau_pertinencia[4])

	return novo_grau_pertinencia


def desenha_grafico(grau_pertinencia):
	if grau_pertinencia is None:
		print 'Conjunto(s) vazio(s)!!'
		return

	legenda = []
	for i,funcao in enumerate(grau_pertinencia):
		if not funcao:
			continue
		elif i == 0:
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