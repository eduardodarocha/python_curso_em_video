# Exercício Python 092: Crie um programa que leia nome, ano de nascimento
# e numero da carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o ano de contratação e o salário. # Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar (35 anos de trabalho).
#
# Python Exercise 092: Create a program that reads name, year of birth and
# work record booklet number and register it (with age) in a dictionary. If
# work record booklet number happens to be unlike ZERO, the dictionary will also
# receive the year of hire and the salary. Calculate and add, in addition
# to age, how old the person will retire (35 years of work).
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')

# Minha solução
# from datetime import date
# anoatual = date.today().year
# dados = dict()
# nome = input('Nome: ')
# nascimento = int(input('Ano de Nascimento: '))
# ctps = int(input('Carteira de Trabalho (0 não tem): '))
# idade = anoatual - nascimento
# dados['nome'] = nome
# dados['idade'] = idade
# dados['ctps'] = ctps
# if ctps == 0:
#     print('-=' * 30)
# else:
#     anocontrat = int(input('Ano de contratação: '))
#     salario = (float(input('Salário: R$ ')))
#     idadeaposenta = ((anocontrat + 35) - anoatual) + idade
#     dados['contratação'] = anocontrat
#     dados['salario'] = salario
#     dados['aposentadoria'] = idadeaposenta
#     print('-=' * 30)
# for k, v in dados.items():
#     print(f'  - {k} tem o valor {v}')
