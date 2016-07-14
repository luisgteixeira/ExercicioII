import numpy as np
import math
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
            cria_universo_discurso()
            conjunto_fuzzy_1 = le_conjunto()
            conjunto_fuzzy_2 = le_conjunto()
            print "Igualdade: " + str(igualdade(conjunto_fuzzy_1, conjunto_fuzzy_2))
            print "Inclusao: " + str(inclusao(conjunto_fuzzy_1, conjunto_fuzzy_2))
            # ---------------------------- #
        elif opcao == '9':
            # Questao 9 ------------------ #
            print '\n----: QUESTAO 9 :----'
            print '\nINSIRA 2 CONJUNTOS FUZZY:'
            cria_universo_discurso()
            # Cria valor de incremento de acordo com o total de pontos da discretizacao
            pontos = 20.0
            discretizacao = (max_U - min_U) / pontos
            # Cria lista com 20 pontos de discretizacao no intervalo do universo de discurso
            universo_discurso = np.arange(min_U, max_U + discretizacao, discretizacao)

            print '-: F1 = (x, 1, 3, 5), funcao de pertinencia triangular :-'
            impressao_questao_9(funcao_triangular(universo_discurso, 1.0, 3.0, 5.0))
            print '-: F2 = (x, 1, 2, 4), funcao de pertinencia triangular :-'
            impressao_questao_9(funcao_triangular(universo_discurso, 1.0, 2.0, 4.0))
            print '-: F3 = (x, 1, 4, 6), funcao de pertinencia triangular :-'
            impressao_questao_9(funcao_triangular(universo_discurso, 1.0, 4.0, 6.0))
            print '-: F4 = (x, 3, 4, 5, 7), funcao de pertinencia trapezoidal :-'
            impressao_questao_9(funcao_trapezoidal(universo_discurso, 3.0, 4.0, 5.0, 7.0))
            print '-: F5 = (x, 1, 3, 2), funcao de pertinencia gaussiana :-'
            impressao_questao_9(funcao_gaussiana(universo_discurso, 1.0, 2.0))
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
    global min_U, max_U

    msg = ''
    grau_de_igualdade = 0.0
    # Preenche com grau de pertinencia igual a 0 as classes inexistentes nos conjuntos
    for c in range(min_U,max_U+1):
        chave = str(c)
        if not chave in conjunto_fuzzy_1.keys():
            conjunto_fuzzy_1[chave] = 0.0
        if not chave in conjunto_fuzzy_2.keys():
            conjunto_fuzzy_2[chave] = 0.0

    for chave in conjunto_fuzzy_1:
        if conjunto_fuzzy_1[chave] != conjunto_fuzzy_2[chave]:
            if abs(conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave]) > grau_de_igualdade:
                grau_de_igualdade = abs(conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave])

    if grau_de_igualdade == 0.0:
        msg += 'Os conjuntos sao iguais. '
    else:
        msg += 'Os conjuntos nao sao iguais. '

    msg += 'Grau de igualdade = ' + str(1 - grau_de_igualdade)

    return msg


def inclusao(conjunto_fuzzy_1, conjunto_fuzzy_2):
    global min_U, max_U

    cardinalidade = float(max_U) - float(min_U) + 1.0
    msg = ''
    grau_de_inclusao = 0.0

    # Preenche com grau de pertinencia igual a 0 as classes inexistentes nos conjuntos
    for c in range(min_U,max_U+1):
        chave = str(c)
        if not chave in conjunto_fuzzy_1.keys():
            conjunto_fuzzy_1[chave] = 0.0
        if not chave in conjunto_fuzzy_2.keys():
            conjunto_fuzzy_2[chave] = 0.0

    for chave in conjunto_fuzzy_1:
        if conjunto_fuzzy_1[chave] <= conjunto_fuzzy_2[chave]:
            grau_de_inclusao += 1.0
        else:
            grau_de_inclusao += 1.0 - ( conjunto_fuzzy_1[chave] - conjunto_fuzzy_2[chave] )

    grau_de_inclusao = grau_de_inclusao / cardinalidade

    if grau_de_inclusao == 1.0:
        msg += 'O conjunto 1 esta incluido no conjunto 2. '
    else:
        msg += 'O conjunto 1 nao esta incluido no conjunto 2. '

    msg += 'Grau de inclusao = ' + str(grau_de_inclusao)

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


def cria_universo_discurso():
    global min_U, max_U

    conjunto = raw_input('Digite o primeiro e ultimo numero do Universo de Discurso (Ex.: 0/4): ')
    conjunto = conjunto.replace(" ", "")
    conjunto = conjunto.split("/")
    min_U = int(conjunto[0])
    max_U = int(conjunto[1])


def funcao_triangular(universo_discurso, a, m, b):
    conjunto_fuzzy = {}
    for x in universo_discurso:
        if x >= a and x < m:
            conjunto_fuzzy[str(x)] = ((x-a)/(m-a))
        elif x >= m and x <= b:
            conjunto_fuzzy[str(x)] = ((b-x)/(b-m))
        else:
            conjunto_fuzzy[str(x)] = 0.0

    return conjunto_fuzzy


def funcao_trapezoidal(universo_discurso, a, m, n, b):
    conjunto_fuzzy = {}
    for x in universo_discurso:
        if x >= a and x < m:
            conjunto_fuzzy[str(x)] = ((x-a)/(m-a))
        elif x >= m and x < n:
            conjunto_fuzzy[str(x)] = 1.0
        elif x >= n and x <= b:
            conjunto_fuzzy[str(x)] = ((b-x)/(b-n))
        else:
            conjunto_fuzzy[str(x)] = 0.0

    return conjunto_fuzzy


def funcao_gaussiana(universo_discurso, m, gama):
    conjunto_fuzzy = {}
    for x in universo_discurso:
        potencial = (x - m) / gama
        math.pow(potencial, 2)
        conjunto_fuzzy[str(x)] = math.exp(-1 * potencial)

    return conjunto_fuzzy


def impressao_questao_9(conjunto_fuzzy):
    print "Altura = " + str(altura(conjunto_fuzzy))
    print "Suporte = " + str(suporte(conjunto_fuzzy).keys())
    print "Nucleo = " + str(nucleo(conjunto_fuzzy).keys())
    print "Fronteiras = " + str(fronteiras(conjunto_fuzzy).keys())
    print "Cardinalidade = " + str(cardinalidade(conjunto_fuzzy))
    print "Pontos de crossover = " + str(pontos_de_crossover(conjunto_fuzzy))
    print "Alfa-corte (= 0.0) = " + str(alfa_corte(conjunto_fuzzy, 0.0).keys())
    print "Alfa-corte (= 0.2) = " + str(alfa_corte(conjunto_fuzzy, 0.2).keys())
    print "Alfa-corte (= 0.4) = " + str(alfa_corte(conjunto_fuzzy, 0.4).keys())
    print "Alfa-corte (= 0.6) = " + str(alfa_corte(conjunto_fuzzy, 0.6).keys())
    print "Alfa-corte (= 0.8) = " + str(alfa_corte(conjunto_fuzzy, 0.8).keys())
    print "Alfa-corte (= 1.0) = " + str(alfa_corte(conjunto_fuzzy, 1.0).keys())
    print "\n"


if __name__ == '__main__':
    main()
