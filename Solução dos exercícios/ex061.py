# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro
# termo e a razão de uma PA(progessão aritmética, mostrando
# os 10 primeiros termos da progressão usando a estrutura "while".

# Python Exercise 061: Redo CHALLENGE 051 by reading the first
# term and the ratio of a AP(arithmetic progression), showing
# the first 10 terms of the progression using the "while" structure.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➝ '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')


#  Minha solução
# termo = int(input('Digite o 1º termo: '))
# razao = int(input('Digite a razão: '))
# cont = 1
# mrazao = 0
# while cont != 11:
#     print(f'{termo + mrazao}', end=' ➤ ')
#     cont += 1
#     mrazao = mrazao + razao
# print('Acabou')

