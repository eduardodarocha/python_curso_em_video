# Exercício Python 098: Faça um programa que tenha uma função
# chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
# Python Exercise 098: Make a program that has a function
# called counter (), which receives three parameters: start, end and step.
# Your program has to perform three counts using the created function:
# a) from 1 to 10, from 1 to 1
# b) 10 to 0, 2 in 2
# c) a personalized count
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)  # Minha versão (ou configuração)
            # do Pycharm não é necessário usar flush
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
print('-=' * 20)
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

# from time import sleep
#
# def contador(inicio, fim, passo):
#     if passo == 0:
#         passo = passo + 1
#     print('-=' * 20)
#     passo = abs(passo)
#     print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
#     if inicio > fim:
#         fim = fim - 1
#         passo = passo * -1
#     else:
#         fim = fim + 1
#     for i in range(inicio, fim, passo):
#         print(i, end=' ')
#         sleep(0.25)
#     print('FIM!')
#
#
# contador(1, 10, 1)
# contador(10, 0, 2)
# print('-=' * 20)
# print('Agora é a sua vez de personalizar a contagem!')
# ini = int(input('Início: '))
# end = int(input('Fim: '))
# step = int(input('Passo: '))
# contador(ini, end, step)
