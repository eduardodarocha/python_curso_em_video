# Exercício Python 091: Crie um programa onde 4 jogadores joguem
# um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final, coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.
#
# Python Exercise 091: Create a program where 4 players play a
# dice and have random results. Save these results in a Python
# dictionary. At the end, put this dictionaryin order, knowing
# that the winner took the highest number on the dice.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dados.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

# Minha solução
# from random import randint
# from time import sleep
# from operator import itemgetter
# dados = {}
# sorted_dados = {}
# temp = ''
# cont = 1
# cont2 = 1
# for cont in range (1, 5):
#     temp = ('jogador'+str(cont))
#     dados[temp] = randint(1,6)
# print('Valores sorteados:')
# for k, v in dados.items():
#     print(f'   O {k} tirou {v} no dado.')
#     sleep(1)
# sorted_dados = dict(sorted(dados.items(), key = itemgetter(1), reverse=True))  # Não foi passado nas aulas,
# print('-=' * 30)                                                                               # necessitei procurar
# print('Ranking dos jogadores')
# for k, v in sorted_dados.items():
#     print(f'{cont2}º lugar: {k} com {v}')
#     cont2 += 1
#     sleep(1)
