# ex054: Crie um programa que leia o ano de nascimento
# de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores de idade.

# ex054: Create a program that reads the birth year of
# seven people. At the end, show how many people have not yet
# reached the age of majority and how many are already of age..

from datetime import date
datahoje = int((date.today()).strftime('%Y')) # datahoje = date.today().year
countmaior = 0
countmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Qual o ano de nascimento da {c}º pessoa: '))
    idademaior = datahoje - nasc
    if idademaior >= 21:
        countmaior = countmaior + 1
    else:
        countmenor = countmenor + 1
print(f'O número de pessoas maiores de 21 anos é: {countmaior}\n'
      f'e o número de pessoas menores de 21 anos é: {countmenor}')

