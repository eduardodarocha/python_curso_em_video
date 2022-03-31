# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# Python Exercise 113: Rewrite the readInt() function that we did in challenge 104,
# now including the possibility of entering an invalid type number.Take advantage
# and also create a function readFloat() with the same functionality.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: pr favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

n1 = leiaInt("Digite um inteiro: ")
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

# Minha solução
# def leiaInt():
#     while True:
#         try:
#             numI = int(input('Digite um número Inteiro: '))
#         except KeyboardInterrupt:
#             print('\033[0;31mO usuário prefiriu não digitar esse valor.\033[m')
#             return 0
#         except:
#             print('\033[0;31mERRO: Por favor digite um número Interio válido.\033[m')
#         else:
#             return numI
#
#
# def leiaFloat():
#     while True:
#         try:
#             numF = float(input('Digite um número Real: '))
#         except KeyboardInterrupt:
#             print('\033[0;31mO usuário prefiriu não digitar esse valor.\033[m')
#             return 0
#         except:
#             print('\033[0;31mERRO: Por favor digite um número Real válido.\033[m')
#         else:
#             return numF
#
#
# numInt = leiaInt()
# numFloat = leiaFloat()
# print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat} .')
