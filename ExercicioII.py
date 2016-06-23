import numpy as np
import matplotlib.pyplot as plt

global min_U, max_U, universo_discurso, titulo

def main():
	global min_U, max_U, universo_discurso, titulo

	# Valor minimo e maximo do universo de discurso
	min_U = 0.0
	max_U = 10.0

	# Valor minimo e maximo dos conjuntos
	min_A = 1.0
	max_A = 3.0
	min_B = 2.0
	max_B = 4.0

	# Cria valor de incremento de acordo com o total de pontos da discretizacao
	pontos = 1000
	discretizacao = (max_U - min_U) / pontos

	# Cria lista com 1000 pontos de discretizacao no intervalo do universo de discurso
	universo_discurso = np.arange(min_U, max_U + discretizacao, discretizacao)

	# Cria lista com o menor e maior valor de cada conjunto
	conjunto_A = [min_A, max_A]
	conjunto_B = [min_B, max_B]
	
	while (True):

		opcao = raw_input('Digite letra do exercicio a ser executada (A-E): ')
		opcao = opcao.upper()

		if opcao == 'A':
			# Letra A ------------------ #
			print '----: LETRA A :----\n'
			titulo = 'Conjunto A'
			mapeia_conjuto(conjunto_A)
			titulo = 'Conjunto B'
			mapeia_conjuto(conjunto_B)
			# -------------------------- #

		elif opcao == 'B':
			# Letra B ------------------ #
			print '----: LETRA B :----\n'
			valor = input('Digite um valor:')
			pertence_conjunto(conjunto_A, valor)
			pertence_conjunto(conjunto_B, valor)
			# -------------------------- #
			
		elif opcao == 'C':
			# Letra C ------------------ #
			print '----: LETRA C :----\n'
			titulo = 'Conjunto A U B'
			uniao(conjunto_A, conjunto_B)
			# -------------------------- #
			
		elif opcao == 'D':
			# Letra D ------------------ #
			print '----: LETRA D :----\n'
			titulo = 'Conjunto A "intersecao" B'
			intersecao(conjunto_A, conjunto_B)
			# -------------------------- #
			
		elif opcao == 'E':
			# Letra E ------------------ #
			print '----: LETRA E :----\n'
			titulo = 'Complemento de A'
			complemento(conjunto_A)
			titulo = 'Complemento de B'
			complemento(conjunto_B)
			# -------------------------- #
		elif opcao == 'SAIR':
			print 'Finalizando execucao...'
			break
		else:
			print 'Comando nao encontrado! Digite novamente'



def uniao(conjunto_A, conjunto_B):
	""
	conjunto_uniao = []
	funcao_caracteristica_A = mapeia_conjuto(conjunto_A,True)
	funcao_caracteristica_B = mapeia_conjuto(conjunto_B,True)

	for i in range(len(universo_discurso)):
		valor = max(funcao_caracteristica_A[i], funcao_caracteristica_B[i])
		conjunto_uniao.append(valor)

	desenha_grafico(conjunto_uniao)


def intersecao(conjunto_A, conjunto_B):
	""
	conjunto_intersecao = []
	funcao_caracteristica_A = mapeia_conjuto(conjunto_A,True)
	funcao_caracteristica_B = mapeia_conjuto(conjunto_B,True)

	for i in range(len(universo_discurso)):
		valor = min(funcao_caracteristica_A[i], funcao_caracteristica_B[i])
		conjunto_intersecao.append(valor)

	desenha_grafico(conjunto_intersecao)


def complemento(conjunto):
	""
	conjunto_complemento = []
	funcao_caracteristica = mapeia_conjuto(conjunto,True)

	for i in range(len(universo_discurso)):
		valor = 1 - funcao_caracteristica[i]
		conjunto_complemento.append(valor)

	desenha_grafico(conjunto_complemento)


def pertence_conjunto(conjunto, valor):
	""
	if not conjunto:
		print "Conjunto e vazio!"
	else:
		if min_U <= valor and max_U >= valor:
			if conjunto[0] <= valor and conjunto[1] >= valor:
				print 'Valor pertence ao Conjunto [', conjunto[0], ',', conjunto[1], ']'
			else:
				print 'Valor nao pertence ao Conjunto [', conjunto[0], ',', conjunto[1], ']'
		else:
			print 'Valor nao pertence ao Universo de Discurso!'



def mapeia_conjuto(conjunto, retorno=False):
	""
	if not conjunto:
		print "Conjunto e vazio!"
	else:
		funcao_caracteristica = []

		for i in range(len(universo_discurso)):
			if universo_discurso[i] >= conjunto[0] and universo_discurso[i] <= conjunto[1]:
				funcao_caracteristica.append(1)
			else:
				funcao_caracteristica.append(0)
	if retorno:
		return funcao_caracteristica
	
	desenha_grafico(funcao_caracteristica)


def desenha_grafico(funcao_caracteristica):
	plt.plot(universo_discurso, funcao_caracteristica, 'ro', color='blue')

	plt.xticks(np.arange(min_U, max_U+2, 1.0))
	plt.yticks(np.arange(0, 2.5, 1))

	axes = plt.gca()
	axes.set_title(titulo)
	axes.set_xlabel('Universo de discurso')
	axes.set_ylabel('Funcao caracteristica')

	plt.show()


if __name__ == '__main__':
    main()