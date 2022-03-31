# Exercício Python 101: Crie um programa que tenha uma função chamada
# voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem
# voto NEGADO(NÃO VOTA), VOTO OPCIONAL e VOTO OBRIGATÓRIO nas eleições.
# Python 101 exercise: Create a program that has a function called
# vote () that will receive as a parameter the year of birth of a
# person, returning a literal value indicating whether a person
# has a DENIED, OPTIONAL and MANDATORY vote in the elections.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))

# Minha solução
# from datetime import datetime
#
#
# def voto(anon):
#     idade = datetime.now().year - anon
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA.'
#     if (16 <= idade < 18) or (idade >= 65):
#         return f'Com {idade} anos: VOTO OPCIONAL.'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
#
#
# anonasc = int(input('Em que ano você nasceu? '))
# print(voto(anonasc))