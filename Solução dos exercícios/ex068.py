# Exercício Python 068: Faça um programa que jogue par ou ímpar com o
# computador. O jogo só será interrompido quando o jogador perder,mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
# Output -> Diga um valor: ___  -> Par ou Impar? [P/I] ___
#
# Python Exercise 068: Make a program that plays even or odd with the
# computer. The game will only be stopped when the player loses, showing
# the total number of consecutive victories he has won at the end of the game.
# Output -> Say a value:___ -> Even or Odd? [P / I]___

from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
print('=-' * 15)

# minha solução
# from random import randint
# print('=-' * 15)
# print('VAMOS JOGAR PAR OU ÍMPAR')
# print('=-' * 15)
# ganhador = True
# qtganhador = 0
# while ganhador == True:
#     escolhacomputador = randint(0, 10)
#     # print(escolhacomputador)
#     escolha = int(input('Diga um valor: '))
#     parouimpar = input('Par ou Impar? [P/I] ').upper()
#     soma = escolha + escolhacomputador
#     paim = soma % 2
#     if paim == 0:
#         pa = 'P'
#         poui = 'PAR'
#     else:
#         pa = 'I'
#         poui = 'ÍMPAR'
#     if pa == parouimpar:
#         qtganhador += 1
#         ganhador = True
#         print('-' * 50)
#         print(f'Você jogou {escolha} e o computador {escolhacomputador}. Total de {soma}, é {poui}.')
#         print('-' * 50)
#         print('Você VENCEU!')
#         print('Vamos jogar outra vez...')
#     else:
#         print('-' * 50)
#         print(f'Você jogou {escolha} e o computador {escolhacomputador}. Total de {soma}, é {poui}.')
#         print('-' * 50)
#         break
# print('Você PERDEU!')
# print('=-' * 15)
# print(f'GAME OVER! Você venceu {qtganhador} vezes')
