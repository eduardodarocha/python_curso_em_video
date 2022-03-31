# Exercício Python 100: Faça um programa que tenha uma lista chamada
# números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
# Python 100 exercise: Make a program that has a list called numbers and
# two functions called draw () and somaPar (). The first function will draw
# 5 numbers and place them inside the list and the second function will show
# the sum of all the even numbers drawn by the previous function.
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

# Minha solução
# from random import randint
#
# lista = list()
#
#
# def sorteia(lis):
#     for i in range(0, 5):
#         ratemp = randint(1, 10)
#         lis.append(ratemp)
#     print(f'Sorteando 5 valores da lista: ', end='')
#     for i in lis:
#         print(f'{i}', end=' ')
#     print('PRONTO!')
#     return lis
#     # somapar(lis)
#
#
# def somapar(listapronta):
#     soma = 0
#     for i in listapronta:
#         if i % 2 == 0:
#             soma += i
#     print(f'Somando os valores pares de {listapronta}, temos {soma}')
#
#
# sorteia(lista)
# somapar(lista)
