n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
#media = float((n1 + n2) / 2)
media = (n1+n2)/2
print('A média é: {:.1f}'.format(media))
print(f'A média é: {media:.1f}')
print('A média entre {} e {} é: {}'.format(n1, n2, media))

