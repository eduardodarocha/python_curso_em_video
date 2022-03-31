# Exercício Python 082: Crie um programa que vai ler vários números e
# colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
#
# Python 082 exercise: Create a program that will read several numbers
# and put them in a list. After that, create two extra lists that
# will contain only the even values and the odd values entered,
# respectively. At the end, show the content of the three generated lists.

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i , v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')

# Minha solução
# lista = []
# listapar = []
# listaimpar = []
# resp = 'S'
# while resp in 'Ss':
#     lista.append(int(input('Digite um número: ')))
#     resp = input('Quer continuar: [S/N] ').upper()
# for var in lista:
#     if var % 2 == 0:
#         listapar.append(var)
#     else:
#         listaimpar.append(var)
# print('-=' * 30)
# print(f'A lista completa é {lista}')
# print(f'A lista de pares é {listapar}')
# print(f'A lista de ímpares é {listaimpar}')
