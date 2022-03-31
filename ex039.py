import datetime
nasc = int(input('Digite o ano do seu nascimento: ').strip())
data_atual = datetime.datetime.now()
ano_atual1 = int(data_atual.year)

#print(data_atual.year)
# ano_atual = data_atual.strftime('%Y')
# print(ano_atual)
difer = ano_atual1 - nasc
if difer < 18:
    print(f'Você ainda vai se alistar no serviço militar\n'
          f'Faltam {18 - difer} anos ')
elif difer == 18:
    print('Você precisa se alistar esse ano.')
elif difer > 18:
    print(f'Você já ultrapassou a idade de alistamento militar\n'
          f'Se passaram {abs(18 - difer)} anos')
