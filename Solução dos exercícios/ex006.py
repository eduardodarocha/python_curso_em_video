num = int(input('Digite um número: '))
print('O dobro do numero digitado é: {}, o triplo é: {} e a raiz quadrada é:{}'.format((num*2), (num*3), (num**(1/2))))
print(f'\nO dobro do numero digitado é: {num*2},\no triplo é: {num*3}\ne a raiz quadrada é: {num**(1/2):.2f}')
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada e {:.2f}'.format(num, (num*2), (num*3), pow(num, (1/2))))
