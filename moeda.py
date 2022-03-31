######################################################

# Para Exercicio 109:

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

##############################################

#Para o exercicio 110:

def resumo(valor, aum, des):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:"}{moeda(valor):>11}')
    print(f'{"Dobro do preço:"}{dobro(valor, True):>13}')
    print(f'{"Metade do preço:"}{metade(valor, True):>11}')
    print(f'{aum}% de aumento:{aumentar(valor, aum, True):>12}')
    print(f'{des}% de redução:{diminuir(valor, des, True):>12}')
    print('-' * 30)

def metade(valor, format):
    if format == True:
        return moeda(valor / 2)
    else:
        return valor


def dobro(valor, format):
    if format == True:
        return moeda(valor * 2)
    else:
        return valor


def aumentar(valor, porcentagem, format):
    if format == True:
        return moeda(valor + (valor * (porcentagem / 100)))
    else:
        return valor


def diminuir(valor, porcentagem, format):
    if format == True:
        return moeda(valor - (valor * (porcentagem / 100)))
    else:
        return valor


def moeda(real):
    valort = f'R${real:.2f}'
    return valort.replace('.', ',')
