real = float(input('Quanto dinheiro você tem na carteira: R$'))
dolar = (real / 3.27)
dolaratual = real / 5.22 #cotação em 07/04/20
euro = real / 5.69 #cotação em 07/04/20
iene = real / 0.048 #cotação em 07/04/20
print('Você pode comprar $: %.2f' % (dolar))  # método antigo
print('Voce pode comprar ${:.2f}'.format(dolar))
print(f'Você pode trocar R${real:.2f} por ${dolar:.02f}\n')
print(f'Com R${real:.2f} você pode comprar (cotação de 07/04/20):\n'
      f'U${dolaratual:.2f}\n€{euro:.2f}\n¥{iene:.2f}')

