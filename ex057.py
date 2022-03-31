# Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

# Python Exercise 057: Make a program that reads a person's gender,
# but only accepts the 'M' or 'F' values. If it is wrong,
# ask for the typing again until it has a correct value.

# minha resolução
sexo = ''
while (sexo != 'M') and (sexo != 'F'):
    sexo = str(input('Digite o sexo[M/F]: ')).upper()
    if (sexo != 'M') and (sexo != 'F'):
        print('Digite a opção correta por favor[M/F]!')
print(f'O sexo digitado foi {sexo}')

# sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Dados inválidos. Por favor, informar seu sexo: ')).strip().upper()[0]
# print('Sexo {} registrado com sucesso'.format(sexo))


