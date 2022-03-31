# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco
# valores numéricos e cadastre-os em uma lista, já na posição correta de
# inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Python Exercise 080: Create a program where the user can type five numerical
# values and register them in a list, already in the correct position insertion
# (without using sort ()). At the end, show the ordered list on the screen.

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:  # or n > lista[len(lista)-1]
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionado na posição {pos} da lista... ")

                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

#Minha solução
# lista = [0, 0, 0, 0, 0]
# cont = 0
# while cont < 5:
#     valor1 = int(input('Digite um valor: '))
#     if valor1 > lista[4]:
#         lista.insert(5, valor1)
#         lista.pop(0)
#         print(f'Adicionado ao final da lista...')
#         print(lista)
#     elif valor1 > lista[3]:
#         lista.insert(4, valor1)
#         lista.pop(0)
#         print(f'Adicionado na posição 4...')
#         print(lista)
#     elif valor1 > lista[2]:
#         lista.insert(3,valor1)
#         lista.pop(0)
#         print(f'Adicionado na posição 3...')
#         print(lista)
#     elif valor1 > lista[1]:
#         lista.insert(2, valor1)
#         lista.pop(0)
#         print(f'Adicionado na posição 2...')
#         print(lista)
#     else:
#         lista.insert(1, valor1)
#         lista.pop(0)
#         print(f'Adicionado na posição 1...')
#         print(lista)
#     cont = cont + 1
# print(f'contador 2 = {cont}')
