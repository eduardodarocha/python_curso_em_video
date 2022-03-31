# Exercício Python 090: Faça um programa que leia nome e
# média de um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da estrutura a seguir na tela.
# Nome: (entrar com nome do aluno)
# Média de ('nome inputado'): (entrar com média)
# Nome é igual a ('nome inputado')
# Média é igual a ('media inputada')
# Situação é igual a ('Reprovado se < 6 ou Aprovado >= 6')
#
# Python Exercise 090: Make a program that reads the name and average
# grade of a student, also keeping the situation in a dictionary.
# At the end, show the content of the structure on the screen.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

#Minha solução
# dado = {}
# dado['nome'] = input('Nome: ')
# dado['media'] = float(input(f'Média de {dado["nome"]}: '))
# print('-=' * 30)
# print(f'  - Nome é igual a {dado["nome"]}')
# print(f'  - Média é igual a {dado["media"]}')
# if dado["media"] >= 7:
#     print('  - Situação é igual a Aprovado')
# elif 5 <= dado['media'] < 7:
#     print('  - Situação é igual a Recuperação')
# else:
#     print('  - Situação é igual a Reprovado')


