# Exercício Python 067: Faça um programa que mostre a tabuada de vários
# números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.
#
# Python Exercise 067: Make a program that shows the multiplication table
# of several numbers, one at a time, for each value entered by the user.
# The program will be interrupted when the requested number is negative.

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')

# Minha solução
# while True:
#     valor = int(input('Quer ver a tabuada de que valor? ').strip())
#     print('-' * 32)
#     if valor < 0:
#         break
#     cont = 0
#     while cont <= 9:
#         cont += 1
#         print(f'{valor} x {cont:>2} = {(valor * cont):>3}')
#     print('-' * 32)
# print('PROGRAMA TABUADA ENCERRADO. Volte sempre! ')