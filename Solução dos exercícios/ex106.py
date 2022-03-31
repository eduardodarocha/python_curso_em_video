# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do
# Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
# usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
#
# Python Exercise 106: Make a mini-system that uses Interactive Help Python.
# The user will enter the command and the manual will appear. When the
# user enters the word 'END', the program will end. Important: use colors.
from time import sleep
c = ('\033[m',  # 0  - Sem cores
     '\033[0;30;41m',  # 1  - vermelho
     '\033[0;30;42m',  # 1  - verde
     '\033[0;30;43m',  # 1  - amarelo
     '\033[0;30;44m',  # 1  - azul
     '\033[0;30;45m',  # 1  - roxo
     '\033[7;30m'  # 1  - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#  Program principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
#
#
# # Minha soução
# def titulo(frase, cor, com=False):
#     if cor == 'azul':
#         color = '\033[1;30;44m'
#     if cor == 'vermelho':
#         color = '\033[30;41m'
#     if cor == 'verde':
#         color = '\033[1;30;42m'
#     if com:
#         print(f'{color}~' * (len(frase) + len(com) + 4))
#         #tam = len(frase) + len(com) + 4
#         print(f"{(frase + com):^{len(frase) + len(com) + 4}}")
#         print(f'{color}~' * (len(frase) + len(com) + 4))
#     else:
#         print(f'{color}~' * (len(frase) + 4))
#         print(f'{frase:^{len(frase) + 4}}')
#         print('~' * (len(frase) + 4))
#     print('\033[0m', end='')
#     sleep(1)
#
#
# def funcIntHelp():
#     while True:  # != 'fim':
#         titulo('SISTEMA DE AJUDA PyHELP', 'verde')
#         biblifun = input('Função ou Biblioteca > ').lower()
#         if biblifun == 'fim':
#             titulo('ATÉ LOGO!', 'vermelho')
#             break
#         titulo('Acessando o manual do comando ', 'azul', biblifun)
#         print("\033[1;7;30m", end='')
#         help(biblifun)
#         print('\033[0m', end='')
#         sleep(2)
#     return
# funcIntHelp()
