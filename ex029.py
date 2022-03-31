velo = int(input('Qual a velocidade do veículo: ').strip())
if velo > 80:
    multa = int((velo - 80) * 7)
    print('Você excedeu o limite de velocidade e foi multado.')
    print(f'O valor da multa foi de R${multa:.2f}')
else:
    print('Tenha um bom dia e não ultrapasse o limie de velocidade')

