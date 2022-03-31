# Minha solução usando o número como string
# num = str(input('Digite um número entre 0 e 9999 : '))
# num1 = num.zfill(4)
# numlista = ' '.join(num1).split()
# print(f'Unidades: {numlista[3]}')
# print(f'dezenas: {numlista[2]}')
# print(f'centenas: {numlista[1]}')
# print(f'milhar: {numlista[0]}')

#  Solução encontrada na web usando numeros inteiros
# numat = int(input('Digite um numero (matemático) de 0 até 9999: '))
# unid = int(numat % 10)
# dez = (numat - unid)/10
# dez1 = int(dez % 10)
# cen = (dez-dez1)/10
# cen1 = int(cen % 10)
# mil = (cen-cen1)/10
# mil1 = int(mil % 10)
# print(f'unidade: {unid}')
# print(f'dezena: {dez1}')
# print(f'centena: {cen1}')
# print(f'milhar: {mil1}')

#  Solução do Curso em Videos
num = int(input('Digite um número entre 0 e 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')



