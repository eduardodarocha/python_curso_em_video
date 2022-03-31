print('=:=' * 15)
print('  Calculadora de conversão de base numérica')
print('=:=' * 15)
numint = int(input('Digite um número inteiro para conversão: ').strip())
escolha = int(input('\nDgite uma opção para coverter em outra base numérica: \n'
                    '\33[1;3;30;44m1\33[m -> binário\n'
                    '\33[1;3;30;44m2\33[m -> octal\n'
                    '\33[1;3;30;44m3\33[m -> hexadecimal\n'
                    '->'))
if escolha == 1:
    x = format(numint,'b')
    print(f'O numero {numint} é {x} em binário') #.format(numint, x)
    print(f'O {numint} em decimal, na base binária é {bin(numint)}')
    print(f"O numero {numint} em binario é: {numint:b}")
elif escolha == 2:
    y = oct(numint)
    print(f'O número {numint} em octal é {numint:o} ou {y}')
elif escolha == 3:
    z = hex(numint)
    print(f'O número {numint} em hexadecimal é {numint:x} ou {z} ou {z[2:]}')
else:
    print('Opção inválida, tente outra vez.')