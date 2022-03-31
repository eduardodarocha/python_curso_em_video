# Exercício Python 065: Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.

# Python Exercise 065: Create a program that reads several intregers numbers
# from the keyboard. At the end of the run, show the average of all values
# and which was the highest and lowest values read. The program should ask
# the user whether he wants to continue to enter values or not.

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continua? [S/N] ')).upper().strip()
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
# saida = 'N'
# soma = cont = maior = menor = 0
# while saida != 'S':
#     num = int(input('Digite um número: ').strip())
#     soma = soma + num
#     cont +=1
#     if cont == 1:
#         maior = num
#         menor = num
#     else:
#         if maior < num:
#             maior = num
#         elif menor > num:
#             menor = num
#     saida = str(input('Você quer sair[S/N]: ').upper())
# print(f'Você digtou {cont} números.')
# print(f'O maior número foi o {maior} e o menor foi o {menor}')
# print(f'A média dos números digitados foi {soma/cont:.2f}')


