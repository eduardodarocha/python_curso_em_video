# Exercício Python 076: Crie um programa que tenha uma tupla única com
# nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados em forma tabular.
# Python Exercise 076: Create a program that has a single tuple
# withproduct names and their respective prices, below. At the
# end, show a price listing, organizing the data in tabular form.

listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'Régua', 1.1,
            'Hidrocor', 4.90, 'Tesoura escolar', 1.99, 'Dicionário(peq)', 5.9, 'Notebook', 1835 )
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos %2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

#Minha solução
# listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
#             'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'Régua', 1.1, 'Hidrocor', 4.90, 'Tesoura escolar',
#             1.99, 'Dicionário(peq)', 5.9, 'Notebook', 1835 )
# print('-' * 40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-' * 40)
# tamanho = len(listagem)
# cont = 0
# cont1 = 1
# while cont < tamanho:
#     print(f'{listagem[cont]:.<30}R${listagem[cont1]:>7.2f}')
#     cont += 2
#     cont1 += 2
# print('-' * 40)
