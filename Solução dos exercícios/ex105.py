# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
#
# Python Exercise 105: Make a program that has a notes function ()
# that can receive multiple grades from students and will return a dictionary
# with the following information:
# - Quantity of notes
# - The highest grade
# - The lowest grade
# - The class average
# - The situation (optional)
# Also add the docstrings for this function for consultation by the developer.

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param dados: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# Programa principal
# resp = notas(5.5, 2.5, 9, 8.5)
resp = notas(5.5, 2.5, 2, 8.5, sit=True)
print(resp)
# help(notas)



# Minha solução
# def notas(* dados, sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param dados: uma ou mais notas dos alunos (aceita várias)
#     :param sit: valor opcional, indica se deve ou não adicionar a situação.
#     :return: dicionário com várias informações sobre a situação da turma.
#     """
#     listadados = dict()
#     tam = len(dados)
#     listadados['total'] = tam
#     maior = menor = 0
#     somanotas = 0
#     for valor in dados:
#         somanotas += valor
#         if valor == dados[0]:
#             maior = valor
#             menor = valor
#             cont =+ 1
#         else:
#             if valor > maior:
#                 maior = valor
#             if valor < menor:
#                 menor = valor
#     media = somanotas / tam
#     listadados['maior'] = maior
#     listadados['menor'] = menor
#     listadados['média'] = media
#     if sit:
#         if media >= 7:
#             situa = 'BOA'
#         elif  7 > media >= 5:
#             situa = 'RAZOÁVLE'
#         else:
#             situa = 'RUIM'
#         listadados['situação'] = situa
#     return listadados


# Programa Principal
# #resp = notas(3.5, 2, 6.5, 2, 7, 4)
# resp = notas(5.5, 9.5, 10, 6.5, sit=True)
# print(resp)
# help(notas)