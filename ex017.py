from math import sqrt, pow, hypot  # ou "import math"

catadj = float(input('Digite o valor do cateto adjacente: '))
catopo = float(input('Digite o vaor do cateto oposto: '))
hipo = sqrt(pow(catadj, 2) + pow(catopo, 2))
hipofacil = (catadj ** 2 + catopo ** 2) ** (1/2)
print(f'A hipotenusa de um triângulo com os catetos {catadj} e {catopo} é: {hipo}')
print('A hipotenusa calculada no modo fácil é: ', hipofacil)
print('A hipotenusa do cateto oposto {} e cateto adjacente {} é --> {}'.format(catopo, catopo, hypot(catopo, catadj)))

