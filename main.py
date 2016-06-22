import numpy as np
import matplotlib.pyplot as plt

def main():
	min_u = 0.0
	max_u = 10.0

	min_a = 1
	max_a = 3
	min_b = 2
	max_b = 4

	pontos = 1000

	# discretizacao = (max_u - min_u) / pontos
	discretizacao = 2

	funcao_caracteristica = np.arange(min_u, max_u, discretizacao)
	universo_discurso = [0,1,1,1,0]

	desenhaGrafico(min_u, max_u, funcao_caracteristica, universo_discurso)


def desenhaGrafico(min_u, max_u, funcao_caracteristica, universo_discurso):
	plt.plot(funcao_caracteristica, universo_discurso, 'ro')
	plt.axis([min_u-1, max_u+1, 0, 1.5])
	plt.show()


if __name__ == '__main__':
    main()
