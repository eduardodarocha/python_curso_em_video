# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador
# de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o campeonato.
#
# Python 093 Exercise: Create a program that manages a player's performance of football.
# The program will read the player's name and how many matches he has played. After will
# read the number of goals scored in each match. In the end, all of that will be saved
# in a dictionary, including the total goals scored during the championship.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas jogou {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quanto gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de { jogador["total"]} gols.')

# Minha solução
# dados = {}
# golstemp = []
# totalgols = 0
# dados['nome'] = input('Nome do Jogador: ')
# partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
# for c in range(0, partidas):
#     golstemp.append(int(input(f'Quantos gols na partida {c}? ')))
#     totalgols = totalgols + golstemp[c]
# dados['gols'] = golstemp
# dados['total'] = totalgols
# print('-=' * 30)
# print(dados)
# print('-=' * 30)
# for k, v in dados.items():
#     print(f'O campo {k} tem o valor {v}.')
# print('-=' * 30)
# print(f'O Jogador {dados["nome"]} jogou {partidas} partidas.')
# for c, v in enumerate(dados['gols']):
#     print(f'    => Na partida {c}, fez {v} gols.')
# print(f'Foi um total de {dados["total"]} gols.')
