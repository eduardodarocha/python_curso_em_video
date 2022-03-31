# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')
# Python Exercise 104: Create a program that has the readInt () function,
# which will work similarly to Python's input () function, only doing the
# validation to accept only a numeric value.
# Ex: n = LeiaInt ('Type an n:')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

# Minha solução
# def leiaInt(frase):
#     print('-' * 30)
#     while True:
#         numeroint = input(frase)
#         if numeroint.isdigit():
#             return numeroint
#         else:
#             print('\033[31m' + 'ERRO! Digite um número inteiro válido.' + '\033[0m')


# Programa principal
# n = leiaInt('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')
