sal = float(input('Qual é o seu salário: R$'))
salau = float(sal+(sal*0.15))
print(f'O seu novo salário com 15% de aumento é: R${salau:.02f}')

preco = float(input('Qual o preço do produto: R$'))
precodesc = preco - (preco * 10 / 100)
precoprazo = preco + (preco * 8 / 100)
print('O preço do produto com desconto é R${:.2f} e a prazo é R${:.2f}'.format(precodesc, precoprazo))