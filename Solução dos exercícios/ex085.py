# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha separados os valores
# pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# Python 085 exercise: Create a program where the user can enter seven values
# numeric values and register them in a single list that keeps the even values
# separate and odd. At the end, show even and odd values in ascending order.

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Todos os valores pares digitados: {num[0]}')
print(f'Todos os valores ímpares digitados: {num[1]}')

'''Minha solução'''
# listanum = [[], []]
# for num in range(1, 8):
#     valor = int(input(f'Digite o {num}º valor: '))
#     if valor % 2 == 0:
#         listanum[0].append(valor)
#     else:
#         listanum[1].append(valor)
# print('-=' * 30)
# listanum[0].sort()
# listanum[1].sort()
# print(f'Os valores pares digitados foram: {listanum[0]}')
# print(f'Os valores ímpares digitados foram: {listanum[1]}')