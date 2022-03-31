print(f'{" Lojas Guanabara ":=^40}')#.format (' Lojas Guanabara '))
preco = float(input('Qual o preço do produto: ').strip())
print('Escolha a condição de pagamento: \n'
      '\033[4;7;34m[1]\033[m- A Vista em dinheiro\cheque: 10% de desconto.\n'
      '\033[4;7;34m[2]\033[m- A Vista no cartão: 5% de desconto. \n'
      '\033[4;7;34m[3]\033[m- Até 2x no cartão:Sem desconto.\n'
      '\033[4;7;34m[4]\033[m- 3x ou mais no cartão: 20% de juros.')
condicao = int(input('Condição de pagamento ==> ').strip())
if condicao == 1 or condicao == 2:
    if condicao == 1:
        preco1 = preco - (preco * 10 / 100)
        print(f'O preço a vista em dinheiro/cheque é R${preco1:.2f} ')
    elif condicao == 2:
        preco2 = preco - (preco * 5 / 100)
        print(f'O preço a vista no cartão é R${preco2:.2f}')
else:
    prestacao = int(input('Quantas prestações: '))
    if condicao == 3 and prestacao == 2:
        print(f'O preço em até 2x no cartão é R${preco:.2f}')
        print(f'A prestação será de R${preco / prestacao:.2f}')
    elif condicao == 4:
        preco4 = preco + (preco * 20 / 100)
        print(f'O preço em {prestacao}x ou mais no cartão é R${preco4:.2f}')
        print(f'O valor da prestação em {prestacao}X é de R${preco4 / prestacao:.2f}')
