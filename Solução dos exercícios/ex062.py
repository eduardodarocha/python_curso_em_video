# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o
# usuário se ele quer mostrar mais alguns termos. O programa
# encerrará quando ele disser que quer mostrar 0 termos.

# Python Exercise 062: Improve CHALLENGE 061 by asking the
# user if he wants to show some more terms. The program
# will end when he says he wants to show 0 terms.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} ➝ '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))




# Minha solução
# termo = int(input('Digite o 1º termo: '))
# razao = int(input('Digite a razão: '))
# cont = 1
# mrazao = 0
# cont1 = 0
# while cont != 11:
#     if cont != 10:
#         print(f'{termo + mrazao}', end=' ➤ ')
#         cont += 1
#         mrazao = mrazao + razao
#     else:
#         print(f'{termo + mrazao}', end='')
#         cont += 1
#         mrazao = mrazao + razao
# novo = int(input('\nVocê que mostrar mais quantos termos: '))
# if novo != 0:
#     while novo != 0:
#         while cont1 != novo:
#             if cont1 != (novo - 1):
#                 print(f'{termo + mrazao}', end=' ➤ ')
#                 cont1 += 1
#                 mrazao = mrazao + razao
#             else:
#                 print(f'{termo + mrazao}', end='')
#                 cont1 += 1
#                 mrazao = mrazao + razao
#             # print(f'{termo + mrazao}', end=' ➤ ')
#             # cont1 = 0
#             # mrazao = mrazao + razao
#         novo = int(input('\nVocê que mostrar mais quantos termos: '))
#         cont1 = 0
# print('Acabou')
