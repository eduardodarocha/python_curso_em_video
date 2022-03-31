# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites foram necessários para vencer.

# Python Exercise 058: Improve the CHALLENGE 028 game where the computer will "think"
# of a number between 0 and 10. Only now the player will try to guess until he
# gets it right, showing in the end how many guesses it took to win.

# minha solução
# import random
#
# i = 0
# minhaesc = ''
# computesc = random.randint(0, 10)
# print('O computador pensou em um número entre 0 e 10, tente adivinhar.')
# while computesc != minhaesc:
#     minhaesc = int(input('Qual foi o numero escolhido pelo computador: ').strip())
#     i += 1
#     if minhaesc != computesc:
#         print('Você errou tente outra vez')
# if i == 1:
#     print('\033[34mVocê acertou de primeira')
# else:
#     print(f'\033[31mVocê acertou mas precisou de {i} tentativas')

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    # else:
    #     if jogador < computador:
    #         print('Mais... Tente mais uma vez.')
    #     elif jogador > computador:
    #         print('Menos... Tente mais uma vez.')
print('Acertou com {} tentatias. Parabéns!'.format(palpite))