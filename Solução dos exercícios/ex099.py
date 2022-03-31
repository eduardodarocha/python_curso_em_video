# Exercício Python 099: Faça um programa que tenha uma função chamada
# maior(), que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.
# Python Exercise 099: Make a program that has a function called greater (),
# which receives several parameters with integer values. Your program
# you have to analyze all the values and say which one is the highest.
from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


# Minha solução
# from time import sleep

# def maior(*num):
#     cont = 0
#     #     print(num)
#     #     print(max(num))
#     print('-=' * 20)
#     print('Analisando os valores passados...')
#     for i in num:
#         cont += 1
#         print(f'{i}', end=' ')
#         sleep(0.3)
#     print(f'Foram informados {cont} valores ao todo.')
#     if cont == 0:
#         print(f'O maior valor informado foi 0.')
#     else:
#         print(f'O maior valor informado foi {max(num)}.')

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
