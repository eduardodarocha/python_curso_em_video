# Exercício Python 084: Faça um programa que leia nome e peso de
# várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# Python exercise 084: Make a program that reads the names and weight
# of several people, keeping everything in a list. At the end, show:
# A) How many people have been registered.
# B) A list with the heaviest people.
# C) A list with the lightest people.

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

'''Minha solução'''
# nomepeso = list()
# listatemp = []
# pesomaior  = list()
# pesomenor = list()
# dado = []
# quant = 0
# cont = 0
# maior = menor = 0
# while True:
#     listatemp.append(str(input('Nome: ')))
#     listatemp.append(float(input('Peso: ')))
#     nomepeso.append(listatemp[:])
#     listatemp.clear()
#     continuar = input('Quer continuar? [S/N] ')
#     quant += 1
#     if continuar in "Nn":
#         break
# for c in nomepeso:
#     if cont == 0:
#         maior = c[1]
#         print(f'maior é ==> {maior}')
#         menor = c[1]
#         dado.append(c[0])
#         pesomaior.append(dado[:])
#         pesomenor.append(dado[:])
#         dado.clear()
#         cont += 1
#     else:
#         if c[1] == maior:
#             dado.append(c[0])
#             pesomaior.append(dado[:])
#             dado.clear()
#         if c[1] > maior:
#             pesomaior.clear()
#             dado.append(c[0])
#             pesomaior.append(dado[:])
#             dado.clear()
#             maior = c[1]
#         elif c[1] == menor:
#             dado.append(c[0])
#             pesomenor.append(dado[:])
#             dado.clear()
#         elif c[1] < menor:
#             pesomenor.clear()
#             dado.append(c[0])
#             pesomenor.append(dado[:])
#             dado.clear()
#             menor = c[1]
#         cont += 1
# print('=-' * 30 )
# print(f'Ao todo, você cadastrou {quant} pessoas')
# print(f'O maior peso foi {maior}kg. Peso de ', end='')
# for s in pesomaior:
#     print(f'{s}', end='')
# print('')
# print(f'O menor peso foi {menor}kg. Peso de ', end='')
# for n in pesomenor:
#     print(f'{n}', end='')
