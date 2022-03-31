#  ex048: Faça um programa que calcule a soma entre todos os números
#  que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# ex048: Make a program that calculates the sum between all numbers
# which are multiples of three and in the range of 1 to 500.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1  # (ou) cont += 1
        soma = soma + c  # (ou) cont += c
print(f'A soma de todos os {cont} números solicitados é {soma}')