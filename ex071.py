# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o
# programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# Output -> Qual o valor a ser sacado: R$___  ->
# Total de ___ cédulas de R$(50 ou 20...)
# Total de ___ cédulas de R$(20 ou 10...)
# Total de ___ cédulas de R$(10 ou 1...)
# Total de ___ cédulas de R$(1)
#
# Python Exercise 071: Create a program that simulates the functioning of an ATM.
# At the beginning, ask the user what will be the amount to be withdrawn (whole number)
# and the program will inform how many bills of each amount will be delivered.
# OBS: consider that the cash has notes of  $50, $20, $10 and $1.
# Output -> What is the amount to be withdrawn: $ ___ ->
# # Total ___ $ banknotes $(50 or 20 ...)
# # Total ___ $ banknotes $(20 or 10 ...)
# # Total ___ $ banknotes $(10 or 1 ...)
# # Total ___ $ banknotes $(1)

# print('=' * 30)
# print('{:30}'.format('BANCO CEV'))
# print('=' * 30)
# valor = int(input('Que valor você quer sacar? R$'))
# total = valor
# ced = 50
# totced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totced += 1
#     else:
#         if totced > 0:
#             print(f'Total de {totced} cédulas de R${ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totced = 0
#         if total == 0:
#             break
# print('=' * 30)
# print('Volte sempre ao Banco CEV! Tenha um bom dia!')



print('=' * 35)
print(f'{"BANCO CEV":^35}')
print('=' * 35)
valor = int(input('Que valor você quer sacar? R$'))
while valor != 0:
    while valor > 0:
        if valor // 50 >= 1:
            nota50 = valor // 50
            valor = valor % 50
            print(f'Total de {nota50} cédulas de R$50')
            break
        elif valor // 20 >= 1:
            nota20 = valor // 20
            valor = valor % 20
            print(f'Total de {nota20} cédulas de R$20')
            break
        elif valor // 10 >= 1:
            nota10 = valor // 10
            valor = valor % 10
            print(f'Total de {nota10} cédulas de R$10')
            break
        elif valor // 1 >= 1:
            nota1 = valor // 1
            print(f'Total de {nota1} cédulas de R$1')
            valor = 0
            break
print('=' * 30)
print('Volte sempre ao Banco CEV! Tenha um bom dia!')