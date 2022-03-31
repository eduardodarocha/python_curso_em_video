# Exercício Python 075: Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
# Python Exercise 075: Develop a program that reads four values
# using the keyboard and store them in a tuple. At the end, show:
# A) How many times did the value 9 appear.
# B) In which position the first value 3 was entered.
# C) What were the even numbers.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitador foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



#Minha solução
# valor1 = int(input('Digite um número: ').strip())
# valor2 = int(input('Digite outro número: ').strip())
# valor3 = int(input('Digite mais umnúmero: ').strip())
# valor4 = int(input('Digite o último número: ').strip())
# valores = (valor1, valor2, valor3, valor4)
# print(f'Você digitou os valores: {valores}')
# print(f'O valor 9 apareceu {valores.count(9)} vezes.')
# if 3 in valores:
#     print(f'O valor 3 apareceu na {(valores.index(3)) + 1}º posição')
# else:
#     print('O valor 3 não foi digitado em nenhuma posição')
# i = 0
# print('Os valores pares digitados foram ', end='')
# for i in range(0, 4):
#     if valores[i] % 2 == 0:
#         print(valores[i],end=' ')
