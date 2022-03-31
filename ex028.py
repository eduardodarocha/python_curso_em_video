import random
from time import sleep
print('=x=' * 20)
print('Eu pensei em um número, tente adivinhar...')
print('=x=' * 20)
nrandom = (random.randint(0, 5))
escolha = int(input('Escolha um número de 0 a 5 para ver \nse você descobre qual é: ').strip())
print('Processando...')
sleep(2)
if nrandom == escolha:
    print('Você venceu. Parabéns!\U0001F642')
else:
    print('Você perdeu. Tente outra vez!\U00002639')


