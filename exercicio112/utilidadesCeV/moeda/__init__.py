def resumo(valor, aum, des):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<20}{moeda(valor)}')
    print(f'{"Dobro do preço:":<20}{dobro(valor, True)}')
    print(f'{"Metade do preço:":<20}{metade(valor, True)}')
    print(f'{aum}{"% de aumento:":<18}{aumentar(valor, aum, True)}')
    print(f'{des}{"% de redução:":<18}{diminuir(valor, des, True)}')
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