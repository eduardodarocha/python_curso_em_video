# Exercício Python 064: Crie um programa que leia vários números inteiros
# pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag "999")

# Python Exercise 064: Create a program that reads several intergers numbers
# from the keyboard. The program will only stop when the user enters the
# value 999, which is the stop condition. At the end, show how many numbers
# were entered and what was the sum between them (disregarding the flag "999")

cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

# Minha solução
# num = soma = cont = 0
# while num != 999:
#     num = int(input('Digite um número ou [999] para sair: '))
#     if num != 999:
#         cont += 1
#         soma = soma + num
# print(f'A soma dos números foi {soma}  \na quantidade de números digitados foi {cont}.')
