# ex051: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

# ex051: Develop a program that reads the first term
# and the ratio for an arithmetic progression (AP).
# At the end, show the top 10 terms of this progression.

termo1 = int(input('Digite o primeiro termo: ').strip())
razao = int(input('Digite a razão: '))
for c in range(termo1, (termo1 + (10 * razao)), razao): # (termo1, (termo1+(10 - 1) * razao) + razao, razao)
    print(f'Termo numero {c} ') #  print(f'{c}',end = '-')
print('Acabou')


