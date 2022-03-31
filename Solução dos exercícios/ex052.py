# ex052: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

# ex052: Make a program that reads an whole number
# and say whether or not it is a prime number.

total = 0
num = int(input('Digite o número: '))
for c in range(1, num +1):
    if num % c == 0:
        total = total + 1
if total == 2:
    print(f' O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')

# num = int(input('Digite o número: '))
# tot = 0
# for c in range(1, num + 1):
#     if num % c == 0:
#         print('\033[33m', end='')
#         tot += 1
#     else:
#         print('\033[31m', end='')
#     print('{} '.format(c), end='')
# print('\n\033[mO numero {} foi divisível {}'.format(num, tot))
# if tot ==2:
#     print('E por sso ele é PRIMO!')
# else:
#     print(' E por isso ele NÃO É PRIMO!')
