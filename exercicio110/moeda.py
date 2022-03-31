# Para Exercicio 110:
def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Aumenta o valor em x porcento
    :param preco: valor a ser aumentado
    :param taxa: porcentagem que o parâmetro preço será aumentado
    :param formato: Formata saida para moeda Real e com vírgula
    :return: preço aumentado da taxa
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)

# Minha solução
# Para o exercicio 110:

# def resumo(valor, aum, des):
#     print('-' * 30)
#     print(f'{"RESUMO DO VALOR":^30}')
#     print('-' * 30)
#     print(f'{"Preço analisado:"}{moeda(valor):>11}')
#     print(f'{"Dobro do preço:"}{dobro(valor, True):>13}')
#     print(f'{"Metade do preço:"}{metade(valor, True):>11}')
#     print(f'{aum}% de aumento:{aumentar(valor, aum, True):>12}')
#     print(f'{des}% de redução:{diminuir(valor, des, True):>12}')
#     print('-' * 30)
#
# def metade(valor, format):
#     if format == True:
#         return moeda(valor / 2)
#     else:
#         return valor
#
#
# def dobro(valor, format):
#     if format == True:
#         return moeda(valor * 2)
#     else:
#         return valor
#
#
# def aumentar(valor, porcentagem, format):
#     if format == True:
#         return moeda(valor + (valor * (porcentagem / 100)))
#     else:
#         return valor
#
#
# def diminuir(valor, porcentagem, format):
#     if format == True:
#         return moeda(valor - (valor * (porcentagem / 100)))
#     else:
#         return valor
#
#
# def moeda(real):
#     valort = f'R${real:.2f}'
#     return valort.replace('.', ',')
