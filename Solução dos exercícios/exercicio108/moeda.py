# Para Exercicio 108:
def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def metade(preco=0):
    res = preco / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

# Minha solução
# def metade(valor):
#     return valor / 2
#
#
# def dobro(valor):
#     return valor * 2
#
#
# def aumentar(valor, porcentagem):
#     valor1 = valor + (valor * (porcentagem / 100))
#     return valor1
#
#
# def diminuir(valor, porcentagem):
#     valor1 = valor - (valor * (porcentagem / 100))
#     return valor1
#
#
#  def moeda(real):
#     valort = f'R${real:.2f}'
#     return valort.replace('.', ',')
