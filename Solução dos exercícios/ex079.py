# Exercício Python 079: Crie um programa onde o usuário possa digitar
# vários valores numéricos e cadastre-os em uma lista. Caso o número
# já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.
# Python Exercise 079: Create a program where the user can type several
# numerical values and register them in a list. If the number already
# exists inside, it will not be added. At the end, they will be
# displayed all unique values entered, in ascending order.

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou {numeros}')

#Minha solução
# teste = []
# valores = []
# desejo = 'S'
# while desejo == 'S':
#     teste = int(input('Digite um valor: '))
#     if teste in valores:
#         print('valor duplicado! Não vou adicionar...')
#     else:
#         valores.append(teste)
#         print('Valor adicionado com sucesso...')
#     desejo = input('Deseja continuar? [S/N]').upper()
#     while desejo not in 'SN':
#         desejo = input('Deseja continuar? [S/N]').upper()
# print('-=' * 30)
# print(f'Você digitou os valores {sorted(valores)}') # retorna mas não cria uma nova lista ordenada


