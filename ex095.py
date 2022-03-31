# Exercício Python 095: Aprimore o desafio 93 para que ele
# funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
#
# Python Exercise 095: Enhance challenge 93 so that it
# works with multiple players, including a system for
# viewing details of each player's performance.

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas jogou {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quanto gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERROR! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    => Na partida {i + 1}, fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

# dados = {}
# dadosgerais = []
# golstemp = []
# totalgols = 0
# esc = 'S'
# opcao = ''
# while esc == 'S':
#     dados['nome'] = input('Nome do Jogador: ')
#     partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
#     for c in range (0, partidas):
#         golstemp.append(int(input(f'Quantos gols na partida {c}? ')))
#         totalgols = totalgols + golstemp[c]
#     dados['gols'] = golstemp[:]
#     dados['total'] = totalgols
#     dadosgerais.append(dados.copy())
#     dados.clear()
#     golstemp.clear()
#     totalgols = 0
#     esc = input('Quer continuar? [S/N]').upper()
#     if esc == 'N':
#         break
#     print('-' * 30)
# print('-=' * 30)
# print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<5}')
# print('-' * 40)
# for c, i in enumerate(dadosgerais):
#         print(f'{str(c):>3} {str(i["nome"]):<15} {str(i["gols"]):<15} {str(i["total"]):<5}')
# print('-' * 40)
# while True:
#     opcao = int(input('Mostrar dados de qual jogador? '))
#     if opcao == 999:
#         break
#     elif opcao <= len(dadosgerais):
#         print(f'--LEVANTAMENTO DO JOGADOR {dadosgerais[opcao]["nome"]}')
#         listagols = dadosgerais[opcao]["gols"]
#         for c, g in enumerate(dadosgerais[opcao]["gols"]):
#             print(f'No jogo {c} fez {g} gols.')
#     else:
#         print(f'ERRO! Nao existe jogador com o código {opcao}! Tente novamente')
#     print('-' * 30)
# print('<< VOLTE SEMPRE >>')
