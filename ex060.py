# Exercício Python 060: Faça um programa que leia um número
# qualquer e mostre o seu fatorial. Faça com "while" and "for"
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Python Exercise 060: Make a program that reads any number
# and shows its factorial. Make with "while" and "for"
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print ('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

# minha solução
# usando comando "while"
# num = int(input('Digte o número para o calculo do fatorial: ').strip())
# count = num - 1
# fat = num
# vezes = ''
# while count != 0:
#     vezes = str(vezes) + 'x' + str(count)
#     fat = fat * count
#     count -= 1
# print(f'{num}! = {fat}')
# print(f'{num}! = {num}{vezes} = {fat}')

#  Usando comando "for"
# num = int(input('Digite o número para o calculo do fatorial: '))
# vezes = ''
# fat = 1
# num1 = num
# count = num - 1
# for num in range(num, 0, -1):
#     print(num)
#     if count != 0:
#         vezes = str(vezes) + 'x' + str(count)
#         count -= 1
#     fat = fat * num
# print(f'{num1}!={num1}{vezes}={fat}')
# print(f'O fatorial de {num1} é {fat}')
