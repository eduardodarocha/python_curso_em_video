# Exercício Python 074: Crie um programa que vai gerar cinco números
# aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.
# Python Exercise 074: Create a program that will generate five numbers
# random and put in a tuple. After that, show the list of generated numbers
# and also indicate the lowest and highest values that are in the tuple.

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

#Minha solução
# from random import randint
#
# tup = ()
# for c in range(0, 5):
#     num = (randint(1, 10),)
#     tup = tup + num
# print('Os valores sorteados foram: ', end='')
# for i in tup:
#      print(i,end=' ')
# menor = sorted(tup)
# print(f'\nO maior valor foi: {menor[-1]}')
# print(f'O menor valor foi: {menor[0]}')

# Outras possibilidades
# d = ()
# for c in range(0, 5):
#     d = d + (randint(1, 10),)
# print(d)

# d = ()
# for c in range(0, 5):
#     a = randint(1, 10)
#     d = d + (a,)
# print(d)
# print(type(d))

# b = []
# for c in range(0, 5):
#     a = randint(1, 10)
#     b.append(a,)
# transf = tuple(i for i in b) # or transf = tuple(b)
# print(b)
# print( transf)
# print(type(transf))
