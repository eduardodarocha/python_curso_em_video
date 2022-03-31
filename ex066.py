# Exercício Python 066: Crie um programa que leia números inteiros pelo
# teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre elas (desconsiderando o flag).
# Output -> A soma dos {quantidade de numeros digitados} foi {soma de todos os números digitados}

# Python Exercise 066: Create a program that reads whole numbers from
# the keyboard. The program will only stop when the user enters the value 999,
# which is the stop condition. At the end, show how many numbers were
# entered and what was the sum between them (disregarding the flag).
# Output -> The sum of {amount of numbers entered} was {sum of all numbers entered}

cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')

# minha solução
# cont = soma = num = 0
# while num != 999:
#     num = int(input('Digite um valor (999 para parar): '))
#     if num == 999:
#         break
#     cont += 1
#     soma += num
# print(f'A soma dos {cont} valores foi {soma}.')
