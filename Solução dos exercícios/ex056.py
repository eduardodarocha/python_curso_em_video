# ex056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome
# do homem mais velho e quantas mulheres têm menos de 20 anos.

# ex056: Develop a program that reads the name, age and sex of 4 people.
# At the end of the program, show: the average age of the group, what is the name
# of the older man and how many women are under 20 years old.

# idadetotal = 0
# idademaior = 0
# contfem = 0
# nomemaior = ''
# for c in range(1, 5):
#     nome = input(f'Digite o {c}º nome: ').strip()
#     idade = int(input('Digite a idade: ').strip())
#     sexo = str(input('Digite o sexo(m/f): ').strip())
#     idadetotal = int(idade + idadetotal)
#     if sexo == 'm':
#         if idade >= idademaior:
#             idademaior = idade
#             nomemaior = nome
#     elif sexo == 'f' and idade < 20:
#         contfem = contfem + 1
# if nomemaior == '' and c == 4:
#     print('Não existem homens na lista')
# elif nomemaior != 'null' and c == 4:
#     print(f'O nome do mais idoso é {nomemaior} e sua idade é {idademaior}')
# print(f'A quantidade de mulheres menores de 20 anos é {contfem}')
# print(f'A media de idade do grupo é de {idadetotal / 4}')
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'Ff' and idade < 20:
             totmulher20 =+ 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))