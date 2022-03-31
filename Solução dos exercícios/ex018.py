import math
ang = float(input('Digite o valor do ângulo: '))
angr = math.radians(ang)
seno = math.sin(angr)
cosseno = math.cos(angr)
tangente = math.tan(angr)
print('O ângulo tem o seno de {:.2f},\no cosseno de {:.2f}\ne a tangente de {:.2f}'.format(seno, cosseno, tangente))
