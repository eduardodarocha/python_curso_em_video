# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# Python 087 exercise: Enhance the previous challenge, showing at the end:
# A) The sum of all the even values entered.
# B) The sum of the values in the third column.
# C) The highest value of the second line.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'Omaior valor da segunda coluna é {mai}')

'''Minha solução'''
# matriz = list()
# totalpar = totcol3 = maiorlin2 = 0
# for lin in range(0, 3):
#     linha = []
#     for col in range(0, 3):
#         dados = (int(input(f'Digite um valor para [{lin}, {col}]: ')))
#         if dados % 2 ==0:
#             totalpar += dados
#         if col  == 2:
#             totcol3 += dados
#         if lin == 1:
#             maior = dados
#             if maior > maiorlin2:
#                 maiorlin2 = maior
#         linha.append(dados)
#     matriz.append(linha[:])
# print('-=' * 30)
# for i in range(0,3):
#     print(f'[ {matriz[i][0]} ][ {matriz[i][1]} ][ {matriz[i][2]} ]')
# print('-=' * 30)
# print(f'A soma dos valores pares é {totalpar}')
# print(f'A soma dos valores da terceira coluna é {totcol3}')
# print(f'O maior valor da segunda linha é {maiorlin2}')
