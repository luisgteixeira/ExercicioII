import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():

    while (True):

        opcao = raw_input('Digite a questao do exercicio a ser executada (7, 8 ou 9): ')
        opcao = opcao.upper()

        if opcao == '7':
            # Questao 7 ------------------ #
            print '\n----: QUESTAO 7 :----'
            conjunto_fuzzy = le_conjunto()
            valor_alfa = raw_input('Digite um valor para alfa: ')
            valor_alfa = float(valor_alfa)
            print "\nAltura = " + str(altura(conjunto_fuzzy))
            print "Suporte = " + str(suporte(conjunto_fuzzy).keys())
            print "Fronteiras = " + str(fronteiras(conjunto_fuzzy).keys())
            print "Nucleo = " + str(nucleo(conjunto_fuzzy).keys())
            print "Pontos de crossover = " + str(pontos_de_crossover(conjunto_fuzzy))
            print "Alfa-corte = " + str(alfa_corte(conjunto_fuzzy, valor_alfa).keys())
            print "Cardinalidade = " + str(cardinalidade(conjunto_fuzzy))
            print "Sub-normal -> Normal = " + str(conversao(conjunto_fuzzy)) + "\n"
			# --------------------------- #

        elif opcao == '8':
            # Questao 8 ------------------ #
            print '\n----: QUESTAO 8 :----'
            print '\nINSIRA 2 CONJUNTOS FUZZY:'
            conjunto_fuzzy_1 = le_conjunto()
            conjunto_fuzzy_2 = le_conjunto()
            print "Igualdade: " + str(igualdade(conjunto_fuzzy_1, conjunto_fuzzy_2))
            print "Inclusao: " + str(inclusao(conjunto_fuzzy_1, conjunto_fuzzy_2))
            # ---------------------------- #
        else:
        	print 'Finalizando execucao...'
        	break


def altura(conjunto_fuzzy):
    return max(conjunto_fuzzy.values())


def suporte(conjunto_fuzzy):
    novo_conjunto_fuzzy = {}
    for chave in conjunto_fuzzy.keys():
        if conjunto_fuzzy[chave] != 0.0:
            novo_conjunto_fuzzy[chave] = conjunto_fuzzy[chave]

    return novo_conjunto_fuzzy


def fronteiras(conjunto_fuzzy):
    novo_conjunto_fuzzy = {}
    for chave in conjunto_fuzzy.keys():
        if conjunto_fuzzy[chave] > 0.0 and conjunto_fuzzy[chave] < 1.0:
            novo_conjunto_fuzzy[chave] = conjunto_fuzzy[chave]

    return novo_conjunto_fuzzy


def nucleo(conjunto_fuzzy):
    novo_conjunto_fuzzy = {}
    for chave in conjunto_fuzzy.keys():
        if conjunto_fuzzy[chave] == 1.0:
            novo_conjunto_fuzzy[chave] = conjunto_fuzzy[chave]

    return novo_conjunto_fuzzy


def pontos_de_crossover(conjunto_fuzzy):
    elementos = []
    for chave in conjunto_fuzzy.keys():
        if conjunto_fuzzy[chave] == 0.5:
            elementos.append(chave)

    return elementos


def alfa_corte(conjunto_fuzzy, valor_alfa):
    if valor_alfa < 0.0 or valor_alfa > 1.0:
        return "Valor alfa invalido!"
    else:
        novo_conjunto_fuzzy = {}
        for chave in conjunto_fuzzy:
            if conjunto_fuzzy[chave] >= valor_alfa:
                novo_conjunto_fuzzy[chave] = conjunto_fuzzy[chave]

        return novo_conjunto_fuzzy


def cardinalidade(conjunto_fuzzy):
    cardinalidade = 0.0
    for chave in conjunto_fuzzy.keys():
        cardinalidade += conjunto_fuzzy[chave]

    return cardinalidade


def conversao(conjunto_fuzzy):
    alt = altura(conjunto_fuzzy)
    if alt == 0.0 or not conjunto_fuzzy:
        return "O conjunto e vazio!!"
    else:
        if alt == 1.0:
            return "O conjunto ja e normal!!"
        else:
            for chave in conjunto_fuzzy:
                conjunto_fuzzy[chave] = conjunto_fuzzy[chave] / alt

            return conjunto_fuzzy


def igualdade(conjunto_fuzzy_1, conjunto_fuzzy_2):
    msg = ''
    grau_de_igualdade = 0.0
    lista1 = conjunto_fuzzy_1.keys()
    lista2 = conjunto_fuzzy_2.keys()

    if cmp(lista1.sort(), lista2.sort()) != 0:
        msg += 'Os conjuntos nao sao iguais e nem compartilham do mesmo Universo de Discurso.'
    else:
        # Se as classes dos 2 conjuntos sao iguais
        if cmp(lista1.sort(), lista2.sort()) == 0:
            for chave in conjunto_fuzzy_1:
                if conjunto_fuzzy_1[chave] != conjunto_fuzzy_2[chave]:
                    if (conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave]) > grau_de_igualdade:
                        grau_de_igualdade = conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave]

            if grau_de_igualdade == 0.0:
                msg += 'Os conjuntos sao iguais. '
            else:
                msg += 'Os conjuntos nao sao iguais. '

            msg += 'Grau de igualdade = ' + str(1 - grau_de_igualdade)

    return msg


def inclusao(conjunto_fuzzy_1, conjunto_fuzzy_2):
    min_U = min(min(conjunto_fuzzy_1.keys()), min(conjunto_fuzzy_2.keys()))
    max_U = max(max(conjunto_fuzzy_1.keys()), max(conjunto_fuzzy_2.keys()))
    cardinalidade = int(max_U) - int(min_U)
    msg = ''
    grau_de_inclusao = 0.0
    # Preenche com grau de pertinencia igual a 0 as classes inexistentes nos conjuntos
    for chave in range(int(min_U),int(max_U)+1):
        if not chave in conjunto_fuzzy_1.keys():
            conjunto_fuzzy_1[chave] = 0.0
        if not chave in conjunto_fuzzy_2.keys():
            conjunto_fuzzy_2[chave] = 0.0

    for chave in conjunto_fuzzy_1:
        if conjunto_fuzzy_1[chave] <= conjunto_fuzzy_2[chave]:
            grau_de_inclusao += 1
        else:
            grau_de_inclusao += 1 - ( conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave] )

    if grau_de_inclusao == 1.0:
        msg += 'O conjunto 1 esta incluido no conjunto 2. '
    else:
        msg += 'O conjunto 1 nao esta incluido no conjunto 2. '

    msg += 'Grau de inclusao = ' + str( grau_de_inclusao * (1 / cardinalidade) )

    return msg


def le_conjunto():
    conjunto = raw_input('Digite o conjunto fuzzy (Ex.: 0.1/1 + 0.3/2 + 1.0/3): ')
    conjunto = conjunto.replace(" ", "")
    conjunto = conjunto.split("+")
    conjunto_fuzzy = {}
    for elemento in conjunto:
        el = elemento.split("/")
        conjunto_fuzzy[el[1]] = float(el[0])

    return conjunto_fuzzy


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
