# Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga
#  mostrar os números como um valor monetário formatado.
# Python Exercise 108: Adapt the code of challenge # 107,
# creating an additional function called currency () that can
# display the numbers as a formatted monetary value.

from exercicio108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
