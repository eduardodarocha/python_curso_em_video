# Exercício Python 072: Crie um programa que tenha uma Tupla totalmente
# preenchida com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Python Exercise 072: Create a program that has a tuple fully populated with
# a long count, from zero to twenty. Your program should read a number on
# the keyboard (between 0 and 20) and show it in full.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')

# Minha solução
# extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
#            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# numero = int(input('Digite um número entre 0 e 20: '))
# while True:
#     if numero < 0 or numero > 20:
#         numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
#     else:
#         break
# print(f'Você digitou o número {extenso[numero]}')