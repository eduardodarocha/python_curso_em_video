# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# Python Exercise 059: Create a program that reads two values and displays a menu on the screen:
# [1] add
# [2] multiply
# [3] bigger
# [4] new numbers
# [5] exit the program
# Your program should perform the requested operation in each case.

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao ==2:
        produto = n1 * n2
        print('O resultado etre {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('')
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format (n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

# minha solução
# n1 = float(input('Digite o primeiro número: ').strip())
# n2 = float(input('Digite o segundo número: ').strip())
# escolha = 0
# while escolha != 5:
#     print('''\n===================================
# Selecione no menu abaixo sua opção:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa''')
#     escolha = int(input('Qual opção: ').strip())
#     print(escolha)
#     if escolha == 1:
#         print(f'A soma de {n1} + {n2} = {n1+n2}')
#     elif escolha == 2:
#         print(f'A multiplicação de {n1} x {n2} = {n1*n2}')
#     elif escolha == 3:
#         if n1 > n2:
#             print(f'O número {n1} é o maior.')
#         elif n2 > n1:
#             print(f'O numero {n2} é o maior.')
#         elif n1 == n2:
#             print(f'O números são iguais')
#     elif escolha == 4:
#         n1 = float(input('Digite o primeiro número: ').strip())
#         n2 = float(input('Digite o segundo número: ').strip())
# print('Programa terminado.')

