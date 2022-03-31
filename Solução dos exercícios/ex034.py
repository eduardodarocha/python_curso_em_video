sal = float(input('Qual é o seu salário: R$').strip())
if sal > 1250.00:
    sal1 = sal + sal * 10 / 100
    print(f'O salário com aumento de 10% é R${sal1:.2f}')
else:
    sal2 = sal + sal * 0.15
    print(f'O salário com aumento de 15% é: R${sal2:.2f}')
