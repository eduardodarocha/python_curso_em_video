# ex047: Crie um programa que mostre na tela todos
#  os números pares que estão no intervalo entre 1 e 50.

# ex047:Create a program that shows on the screen all the
# even numbers that are in the range between 1 and 50.

#  Minha solução
for c in range(1, 51):
    if c % 2 == 0:
        print(f'nº {c} é par.')

# for n in range(2, 51, 2):
#     print(n, end=' ')
# print('Acabou')
