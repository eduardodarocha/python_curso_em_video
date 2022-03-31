# Jogo Jokenpô - Pedra / Papel / Tesoura
# print(emoji.emojize(":raised_hand::raised_fist: :victory_hand:"))  # tem que importar emoji
# print(' ✌ ✋ 🤛  💉/ ✌ 🤛 ✋ ✌ ✊ ✋ ✌ ✋ 🤛 ‍')
# print("\N{raised fist}\N{raised hand} \N{victory hand}")
# print("\U0000270a \U0000270c \U0000270b")

from random import randrange

azul = '\033[0;34m'
verm = '\033[0;31m'
ver = '\033[1;32m'
restauracor = '\033[m'
pedra = '\N{raised fist} Pedra'
papel = '\U0000270b Papel'
tesoura = '\N{victory hand} Tesoura'
# print (verm, pedra, restauracor)
print('Jogo Jokenpô - Pedra / Papel / Tesoura')
print('Opções:')
print(f'1 -{azul} {pedra} {restauracor}')
print(f'2 -{azul} {papel} {restauracor}')
print(f'3 -{azul} {tesoura} {restauracor}')
escolha = int(input('Faça a sua escolha ==> ').strip())
escomput = randrange(1, 3)

if escolha == 1 and escomput == 2:
    print(f'Sua escolha foi {azul}, {pedra}, {restauracor} e o computador foi {verm} {papel} {restauracor}')
    print(f'{ver}O Computador ganhou')
elif escolha == 1 and escomput == 3:
    print(f'Sua escolha foi {azul}, {pedra}, {restauracor} e o computador foi {verm} {tesoura} {restauracor}')
    print(f'{ver}Você ganhou')
elif escolha == 2 and escomput == 1:
    print(f'Sua escolha foi {azul}, {papel}, {restauracor} e o computador foi {verm} {pedra} {restauracor}')
    print(f'{ver}Você ganhou')
elif escolha == 2 and escomput == 3:
    print(f'Sua escolha foi {azul}, {papel}, {restauracor} e o computador foi {verm} {tesoura} {restauracor}')
    print(f'{ver}O Computador ganhou')
elif escolha == 3 and escomput == 1:
    print(f'Sua escolha foi {azul}, {tesoura}, {restauracor} e o computador foi {verm} {pedra} {restauracor}')
    print(f'{ver}O Computador ganhou')
elif escolha == 3 and escomput == 2:
    print(f'Sua escolha foi {azul}, {tesoura}, {restauracor} e o computador foi {verm} {papel} {restauracor}')
    print(f'{ver}Você ganhou')
else:
    print(f'{ver}Vocês empataram. Joguem outra vez')

# ===========================================
#     rograma do Gustavo Guanabara
# ===========================================
# from random import randint
# from time import sleep
# itens = ('Pedra', 'Papel', 'Tesoura')
#      minha opção  ==>    itens2 = ('✊', '✋', '✌')
# computador = randint(0, 2)
# print('''Suas opções:
# [0] Pedra
# [1] Papel
# [2] Tesoura''')
# jogador = int(input('Qual a sua opção? ==> '))
# print('JO...')
# sleep(1)
# print('KEN...')
# sleep(1)
# print('PO...')
# sleep(1)
# print('=-' * 25)
# print((f'O computador escolheu {itens[computador]}').center(50))
# print((f'O jogador escolheu {itens[jogador]}').center(50))
# print('=-' * 25)
# if computador == 0:
#     if jogador == 0:
#         print('EMPATE')
#     elif jogador == 1:
#         print('JOGADOR VENCE')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE')
# elif computador == 1:
#     if jogador == 0:
#         print('COMPUTADOR VENCE')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('JOGADOR VENCE')
# elif computador == 2:
#     if jogador == 0:
#         print('JOGADOR VENCE')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE')
#     elif jogador == 2:
#         print('EMPATE')
