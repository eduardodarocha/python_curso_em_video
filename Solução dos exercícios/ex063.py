# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# Python Exercise 063: Write a program that reads any integer N number
# and shows the first N elements of a Fibonacci Sequence on the screen.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} ➝ {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ➝ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➝ FIM ')


# Minha solução
# a = 0
# b = 1
# elem = int(input('Quantos elementos da sequência Fibonaci você quer: ').strip())
# print(a, b, end=' ')
# while elem != 2:
#     c  = a + b
#     print(c , end=' ')
#     a = b
#     b = c
#     elem -= 1
# print('Acabou')
