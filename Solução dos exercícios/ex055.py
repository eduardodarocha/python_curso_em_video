# ex055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

# ex055: Make a program that reads the weight of five people.
# At the end, show what was the highest and lowest weight read.

# peso = float(input(f'Digite o peso da 1º pessoa: '))
# pesomaior = peso
# pesomenor = peso
# for c in range(2, 6):
#     peso = float(input(f'Digite o peso da {c}º pessoa: '))
#     if peso >= pesomaior:
#         pesomaior = peso
#     elif peso <= pesomenor:
#         pesomenor = peso
# print(f'O maior peso é: {pesomaior:.1f}kg')
# print(f'O menor peso é: {pesomenor:.1f}kg')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
