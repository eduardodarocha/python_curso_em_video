import math
from math import trunc
num = float(input('Digite um número: '))
numint = math.trunc(num)
print('A parte inteira de {} é {}'.format(num, numint))
print(f'A parte inteira de {num} é {math.trunc(num)}')
print('A parte inteira de {} é {}'.format(num, trunc(num)))

num1 = float(input('Digite um número: '))  # sem usar a função trunc
print('\nA parte inteira de {} é {}'.format(num1, int(num1)))  # sem usar a função trunc

