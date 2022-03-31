# Exercício Python 086: Crie um programa que declare uma matriz
# de dimensão 3x3 e preencha com valores lidos pelo teclado. No
# final, mostre a matriz na tela, com a formatação correta.
# Python 086 exercise: Create a program that declares an array
# 3x3 dimension and fill in values read by the keyboard. At the
# end, show the matrix on the screen, with the correct formatting.
# OUTPUT ==>
''' 0  [ 1 ][ 2 ][ 3 ]
    1  [ 4 ][ 5 ][ 6 ]
    2  [ 7 ][ 8 ][ 9 ]
         0    1    2   '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

'''Minhas soluções'''
# dados = list()
# matriz = list()
# for lin in range(0,3):
#     linha = []
#     for col in range(0,3):
#         dados = (int(input(f'Digite o valor para [{lin}, {col}]: ')))
#         linha.append(dados)
#     matriz.append(linha[:])
# for i in range(0,3):
#     print(f'[{matriz[i][0]:^5}][{matriz[i][1]:^5}][{matriz[i][2]:^5}]')

'''outra solução'''
# dados = list()
# matriz = list()
# for lin in range(0,3):
#     linha = []
#     for col in range(0,3):
#         dados = (int(input(f'Digite o valor para [{lin}, {col}]: ')))
#         linha.append(dados) #linha.append(dados)
#     matriz.append(linha[:])
# for i in range(0,3):
#     print(f'[{matriz[i][0]:^5}][{matriz[i][1]:^5}][{matriz[i][2]:^5}]')
