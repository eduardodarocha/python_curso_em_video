# Exercício Python 094: Crie um programa que leia nome, sexo e
# idade de várias pessoas, guardando os dados de cada pessoa em
# um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
#
# Python Exercise 094: Create a program that reads name, gender
# and age of several people, storing each person's data in a
# dictionary and all dictionaries in a list. At the end, show:
# A) How many people were registered
# B) The average age
# C) A list of women
# D) A list of people above the average age

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

# Minha solução
# dicdados = {}
# listageral = []
# esc = 'S'
# mediatemp = 0
# totmulheres = []
# tot_acima = []
# while esc in 'S':
#     nome = input('Nome: ')
#     sexo = input('Sexo: [M/F] ').upper()
#     while sexo not in 'MF':
#         print('ERRO! Por favor, digite apenas M ou F.')
#         sexo = input('Sexo: [M/F] ').upper()
#     idade = int(input('Idade: '))
#     dicdados['nome'] = nome
#     dicdados['sexo'] = sexo
#     dicdados['idade'] = idade
#     # print(dicdados)
#     listageral.append(dicdados.copy())
#     dicdados.clear()
#     esc = input('Quer continuar: [S/N] ').upper()
#     while esc not in 'SN':
#         print('ERRO! Responda apenas S ou N.')
#         esc = input('Quer continuar: [S/N] ').upper()
#     if esc == 'N':
#         break
# for c in range(0, len(listageral)):
#     mediatemp = mediatemp + listageral[c]['idade']
#     media = mediatemp / len(listageral)
#     if listageral[c]['sexo'] in 'F':
#         # print(f'lista geral indice sexo = {listageral[c]["sexo"]}')
#         totmulheres.append(listageral[c]['nome'])
#     # print(f' a lista de mulheres é = {totmulheres}')
# for c in range(0, len(listageral)):
#     if (listageral[c]['idade']) > media:
#         tot_acima.append(listageral[c])
#         # print(tot_acima)
# print('-=' * 30)
# print(f'- O grupo tem {len(listageral)} pessoas.')
# print(f'- A média de idade é {media:.2f} anos.')
# print('- As mulheres cadastradas foram ', end='')
# for m in totmulheres:
#     print(f'{m}', end=' ')
# print(f'\n- A lista de pessoas que estão acima da média: ')
# for i in tot_acima:
#     if i['idade'] > media:
#         print(f'nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')
# print('<< ENCERRADO >>')