pr = float(input('Qual é o preço: R$'))
prdesc = (pr-(pr*5/100))
print('O preço com desconto na promoção é: R${:.02f}'.format(prdesc))
