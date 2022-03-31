# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as
# funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça
# também um programa que importe esse módulo e use algumas dessas funções.
# Python Exercise 107: Create a module called coin.py that has the
# built-in functions increase (), decrease (), double () and half (). Make
# also a program that imports this module and uses some of these functions.

from exercicio107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
