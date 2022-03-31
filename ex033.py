n1 = int(input('Digite o 1º numero: ').strip())
n2 = int(input('Digite o 2º número: ').strip())
n3 = int(input('Digite o 3º número: ').strip())
# if n1 >= n2:
#     if n1 >= n3:
#         print(f'O numero {n1} é o maior')
#         if n2 >= n3:
#             print(f'O número {n3} é o menor')
#         else:
#             print(f'O número {n2} é o menor')
#     else:
#         print(f'O número {n3} é o maior')
#         print(f'O número {n2} é o menor')
#
# else:
#     if n2 >= n3:
#         print(f'O número {n2} é o maior')
#         if n1 >= n3:
#             print(f'O número {n3} é o menor')
#         else:
#             print(f'O número {n1} é o menor')
#     else:
#         print(f'O número {n3} é o maior')
#         print(f'O número {n1} é o menor')

maior = n1  # Outra forma de fazer mais fácil
if n2 >= maior:  # https://www.pythonprogressivo.net/2018/02/Recebe-Tres-Numeros-Exibe-Maior-Menor.html
    maior = n2
if n3 >= maior:
    maior = n3
print(f'O maior número é {maior}')

menor = n1
if n2 <= menor:
    menor = n2
if n3 <= menor:
    menor = n3
print(f'O menor número é {menor}')
