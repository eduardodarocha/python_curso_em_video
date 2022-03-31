import datetime

ano = int(input('Digite o ano ou coloque zero para analisar o ano atual: '))
# anox = int((datetime.datetime(ano, 12, 31)).strftime('%j'))
# print(anox)
# if anox == 366:
#     print(f'O ano de {ano} é um ano bissexto.')
# else:
#     print(f'O ano de {ano} não é um ano bissexto.')
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f'O ano de {ano} é um ano bissexto.')
else:
    print(f'O ano de {ano} não é um ano bissexto.')


