"""Exercício Python 088: Faça um programa que ajude um jogador
da MEGA SENA a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta. """

# Python 088 exercise: Make a program that helps a player of
# the MEGA SENA creating guesses. The program will ask how many
# games will be generated and will draw 6 numbers between 1 and 60
# for each game, registering everything in a composite list.

from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você que que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)

'''Minha solução'''
# from time import sleep
# from random import randint
# num = list()
# cont = 0
# linhapal = list()
# print('-' * 30)
# print(f'{"JOGA NA MEGA SENA":^35}')
# print('-' * 35)
# pal = int(input('Quantos jogos você quer que eu soteie? '))
# for c in range(0, pal):
#     num.clear()
#     while cont < 6:
#         numtemp = randint(1, 60)
#         if numtemp not in num:
#             num.append(numtemp)
#             cont += 1
#     cont = 0
#     num.sort()
#     linhapal.append(num[:])
# print(f'{"-=" * 5} SORTEANDO {pal} JOGOS {"=-" * 5}')
# for c, p in enumerate(linhapal):
#     print(f'Jogo {c + 1}: {p} ')
#     sleep(1)
# print(f'{"-=" * 5} < BOA SORTE > {"=-" * 5}')
