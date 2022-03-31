# Exercício Python 078: Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual foi o maior e
# o menor valor digitado e as suas respectivas posições na lista.
#
# Python Exercise 078: Make a program that reads 5 values numbers
# and keep them in a list. At the end, show what the highest and
# lowest value entered and their respective positions in the list.

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite m valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()

# Minha solução
# maiores = []
# menores = []
# lista = []
# for cont in range(0, 5):
#     lista.append(int(input(f'Digite um valor para posição {cont}: ')))
#     if cont == 0:
#         maior = menor = lista[cont]
#     else:
#         if lista[cont] >= maior:
#             maior = lista[cont]
#         if lista[cont] <= menor:
#             menor = lista[cont]
#     cont += 1
# for indice, numeros in enumerate(lista):
#     if numeros == maior:
#         maiores.append(indice)
#     if numeros == menor:
#         menores.append(indice)
# print('=-' * 30)
# print(f'Você digitou os valores {lista}')
# print(f'O maior valor digitado foi {maior} nas posicões ', end='')
# for i in maiores:
#     print(f'{i}... ', end='')
# print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
# for i in menores:
#     print(f'{i}... ', end='')
