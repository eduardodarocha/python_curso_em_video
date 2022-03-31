# Para Exercicio 109:
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

# Minha solução
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

