# Exercício Python 096: Faça um programa que tenha uma função
# chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.
# Python Exercise 096: Make a program that has a function
# called area (), which receives the dimensions of a terrain
# rectangular (width and length) and show the land area.


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

# Minha solução
# def area(lar, com):
#     area = lar * com
#     print(f'A área de um terreno de {lar} x {com} é de {area:.1f}m².')
#
# print('     Controle de Terrenos')
# print('-' * 30)
# largura = float(input('LARGURA (m): '))
# comprimento = float(input('COMPRIMENTO (m): '))
# area(largura, comprimento)
