# Exercício Python 103: Faça um programa que tenha uma função chamada
#  ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido informado corretamente.
# Python Exercise 103: Make a program that has a function called token (),
# which receives two optional parameters: the name of a player and how
# many goals he scored. The program should be able to show the file of
# the player, even if some data was not informed correctly.

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Numero de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

# def ficha(jog, gols):
#     if not jog:
#         jog = '<desconhecido>'
#     if not gols.isnumeric():
#         gols = 0
#     return print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')
#
# print('-' * 30)
# jogador = input('Nome do jogador: ')
# numgols = input('Número de gols: ')
# ficha(jogador, numgols)