# Exercício Python 073: Crie uma tupla preenchida com os
# 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
# Python Exercise 073: Create a tuple filled with
# the top 20 in the Brazilian Football Championship
# Table, in the order of placement. Then show:
# a) The first 5 teams.
# b) The last 4 placed.
# c) Teams in alphabetical order.
# d) In what position is the Chapecoense team.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco da Gama', 'Chapecoense', 'Atlético Mineiro', 'Botafogo', 'Athletico-PR',
         'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético - GO')
# for t in times:
#     print(t)
print('-=' * 15)
print(f' Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}º posição')

# Minha solução
# times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
#          'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza EC', 'Goiás',
#          'Bahia','Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo',
#          'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
# print('=-' * 30)
# print(f'Os 5 primeiros são {times[0:5]}')
# print('=-' * 30)
# print(f'Os 4 últimos são {times[-4:]}')
# print('=-' * 30)
# print(f'Os times em ordem alfabética {sorted(times)}')
# print('=-' * 30)
# posicao = (times.index('Chapecoense')) + 1
# print(f'O Chapecoense esta na {posicao}º posição.')
# print('=-' * 30)
