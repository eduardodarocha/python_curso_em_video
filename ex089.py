# Exercício Python 089: Crie um programa que leia nome e duas
# notas de vários alunos e guarde tudo em uma lista composta. No
# final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.
#
# Python 089 Exercise: Create a program that reads names and two
# notes from multiple students and keep everything in a composite
# list. At the show a bulletin containing the average of each one and
# allow that the user can show each student's grades individually.

"""Um lista geral-> com todos os alunos
uma lista para cada aluno -> dentro da lista geral com cada nome, notas e média
uma lista com as notas dentro da lista de cada aluno ==> ['nome', [nota1, nota2], media]"""

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 interronpe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

# Minha solução
# listlistageral = list()
# listatemp = list()
# notatemp = list()
# media = ''
# cont = ''
# NotaAluno = 0
# while True:
#     nome = input('Nome: ')
#     notatemp.append(float(input('Nota 1: ')))
#     notatemp.append(float(input('Nota 2: ')))
#     media = round((notatemp[0] + notatemp[1]) / 2, 2)
#     listatemp.append(nome)
#     listatemp.append(notatemp[:])
#     listatemp.append(media)
#     listageral.append(listatemp[:])
#     notatemp.clear()
#     listatemp.clear()
#     cont = str(input('Quer continura? [S/N] ').upper())
#     if cont in 'Nn':
#         break
# print('-=' * 40)
# print(f'{"No.":<4} {"NOME":<15} {"MÉDIA":>4}')
# print('-' * 30)
# for ind, dados in enumerate(listageral):
#     print(f'{ind:<4} {dados[0]:<15}{dados[2]:>4.01f}')
#
# while True:
#     print('-' * 35)
#     NotaAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
#     if NotaAluno == 999:
#         break
#     print(f'Notas de {listageral[NotaAluno][0]} são {listageral[NotaAluno][1]}')
#
# print('FINALIZANDO...')
# print('<<< VOLTE SEMPRE >>>')
