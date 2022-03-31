


valor = float(input('Qual o valor do imóvel: ').strip())
salario = float(input('Qual o seu salário: ').strip())
tempo = int(input('Quantos anos para financiar: ').strip())
prestacao = valor / (tempo * 12)
salario30 = salario * 30 / 100
if prestacao > salario30:
    print('Seu empréstimo foi negado pois a prestação ')
    print("calculada  de \33[0;31mR${:.2f}\33[0m é".format(prestacao))
    print(f'maior que 30% do seu salário ==> R${salario30:.2f}')
else:
    print(f'A sua prestação será de R${prestacao:.2f} e o empréstimo será CONCEDIDO')
