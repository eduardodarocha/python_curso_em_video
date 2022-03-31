# Exercício Python 070: Crie um programa que leia o nome e o
# preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não e se a resposta for diferente
# de S ou N, tem que perguntar outra vez. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
#
# Python Exercise 070: Create a program that reads the name
# and price of various products. The program should ask
# if the user will continue or not and if the answer is different
# of Y or N, you have to ask again. At the end, show:
# A) what is the total amount spent on the purchase.
# B) how many products cost more than $ 1000.
# C) what is the name of the cheapest product.

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

# continuar = 'S'
# precomenor = contador = contmaior = precototal = 0
# while continuar in 'S':
#     nomeproduto = input('Nome do Produto: ')
#     precoprod = float(input('Preço: R$'))
#     precototal += precoprod
#     contador += 1
#     if precoprod > 1000:
#         contmaior += 1
#     if contador == 1:
#         precomenor = precoprod
#         nomemenor = nomeproduto
#     else:
#         if precoprod < precomenor:
#             precomenor = precoprod
#             nomemenor = nomeproduto
#     continuar = input('Deseja continuar: [S/N] ').upper()
#     while continuar not in 'SN':
#         continuar = input('Deseja continuar: [S/N] ').upper()
#         if continuar in 'SN':
#             break
# print(f'====== FIM DO PROGRAMA ======')
# print(f'O total da compra foi R${precototal:.2f}')
# print(f'Temos {contmaior} produtos custando mais de R$1000.00')
# print(f'O produto mais barato foi {nomemenor} que custa R${precomenor:.2f}')
