# Exercício Python 102: Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.
# Python Exercise 102: Create a program that has a factorial function ()
# receiving two parameters: the first indicating the number to be calculated
# and another called show, which will be a logical value (optional) indicating
# whether the factorial calculation process will be shown or not on the screen.

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: O valor da Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa principal
print(fatorial(5))
# help(fatorial)


# def fatorial(num, show=False):
#     """
#     -> Calcula o fatorial de um número(num).
#     :param num: número para se calcular o fatorial.
#     :param show: (Opcional) Mostrar ou não a conta.
#     :return: Somente o valor fatorial de um número
#              ou a soma(conta) e o valor fatorial de um número.
#     """
#     fat = 1
#     saida = num
#     for c in range(1, num + 1):
#         fat = fat * c
#     if show:
#         print('-' * 30)
#         for i in range(num - 1, 0, -1):
#             saida = str(saida) + f' x {i}'
#         return f'{saida} = {fat}'
#     else:
#         print('-' * 30)
#         return fat
#
#
# # Programa principal
# # print(fatorial(5))
# help(fatorial)

