kilometragem = int(input('Qual a distancia da viagem em km: ').strip())
if kilometragem <= 200:
    print(f'O preço da passagem é: R${kilometragem * 0.50:.2f} ')
else:
    print(f'O preço da passagem é: R${kilometragem * 0.45:.2f} ')

# preco = kilometragem * 0.50 if kilometragem <= 200 else kilometragem * 0.45         #outra opção como se
# print('O valor da passagem para {}km é de R${:.2f}'.format(kilometragem, preco))    # fosse um operdor ternário
