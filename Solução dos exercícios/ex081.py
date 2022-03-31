# Exercício Python 081: Crie um programa que vai ler vários
# números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
#
# Python 081 exercise: Create a program that will read
# several numbers and put in a list. After that, show:
# A) How many numbers were entered.
# B) The list of values, ordered in descending order.
# C) Whether the value 5 was entered and is or is not in the list.

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista!')

# Minha solução
# resp = 'S'
# cont = 0
# valores = []
# while resp == 'S':
#     valores.append(int(input('Digite um valor: ')))
#     resp = str(input('Quer continuar: [S/N] ').upper())
#     cont += 1
# print('=-' * 30)
# print(f'Você digitou {cont} elementos.')
# valores.sort(reverse=True)
# print(f'Os valores em ordem decrescente são {valores}')
# if 5 in valores:
#     print('O valor 5 faz parte da lista')
# else:
#     print('O valor 5 não foi encontrado na lista.')
