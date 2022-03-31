lar = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = alt * lar
lit = (area/2)
print('A área da parede é: {:.3f}m² e a quantidade de tinta necessária para pintar é: {} litros '.format(area, lit))
print(f'A área da parede é: {area:.02f}m² e a quant. de tinta necessária para pintura é: {lit:.2f} litros')
