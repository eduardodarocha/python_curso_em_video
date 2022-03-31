# Para Exercicio 107:
def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobro(valor):
    res = valor * 2
    return res


def metade(valor):
    res = valor / 2
    return res

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
