# ex050: Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

# ex050: Develop a program that reads six whole numbers and
# show the sum of only those who are even. If the value
# entered is odd, disregard it.

total = 0
for c in range(1, 7):
    numcont = int(input(f'Digite o {c}º número ==> '))
    if numcont % 2 == 0:
        total = total + numcont  # (ou) total += numcont
print(f'A soma dos números pares é {total}')


