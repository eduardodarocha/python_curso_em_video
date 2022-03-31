# Exercício Python 069: Crie um programa que leia a idade e o sexo
# de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20
# Output -> Idade: __ -> Sexo: [M/F] -> Quer continuar? [S/N]___ (se errar
# a digitação o programa pede para entrar de novo até acertar {número
# para idade, Ff ou Mm para Sexo e Ss ou Nn se quer continuar ou não }

# Python Exercise 069: Create a program that reads the age and sex
# of several people. For each registered person, the program should
# ask if the user wants to continue or not. At the end, show:
# A) how many people are over 18 years old.
# B) how many men were registered.
# C) how many women are under 20 years old.
# Output -> Age: __ -> Gender: [M / F] ___ -> Do you want to continue? [Y / N] ____
# (if you misspell, ask to enter again until you hit {number for age,
# Ff or Mm for Sex and Yy or Nn if you want to continue or not}
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anso: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')

# tothomens = maior18 = mulheresmenor20 = 0
# continuar = 'S'
# print('-' * 30)
# print('      CADASTRE UMA PESSOA')
# print('-' * 30)
# while continuar == 'S':
#     idade = input('Idade: ')
#     while idade.isdigit() is False:
#         idade = input('Idade: ')
#         if idade.isdigit() is True:
#             break
#     idade = int(idade)
#     if idade >= 18:
#         maior18 += 1
#     sexo = input('Sexo: [M/F] ').upper()
#     while sexo not in 'MF':  # while (sexo != 'M') and (sexo != 'F'):
#         sexo = input('Sexo: [M/F] ').upper()
#         if sexo == ('M' or 'F'):
#             break
#     if sexo == 'M':
#         tothomens += 1
#     if (sexo == 'F') and (idade < 20):
#         mulheresmenor20 += 1
#     print('-' * 25)
#     continuar = input('Quer continuar? [S/N] ').upper()
#     while continuar not in 'SN':
#         continuar = input('Quer continuar? [S/N] ').upper()
#         # print(continuar)
#         if continuar in 'SN':
#             break
# print(f'====== FIM DO PROGRAMA ======')
# print(f'Total de pessoas com mais de 18 anos: {maior18}')
# print(f'Ao todo temos {tothomens} homens cadastrados.')
# print(f'E temos {mulheresmenor20} mulheres com menos de 20 anos')
