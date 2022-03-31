medida = float(input('Digite a distância em metros: '))
medidacm = float(medida*100)
medidamm = float(medida*1000)
medidakm = (medida/1000)
medidahm = (medida/100)
medidadan = medida/10
medidadm = medida*10
print('A distância em quilometros é: {}km\nA distância em hectômetro é: {}hm\nA distância em decâmetro é: '
      '{}dam\nA medida em decímetro é: {}dm\nA distância em centímetros é: {:.2f}cm,\nA medida em milímetro é: {:.2f}mm'
      .format(medidakm, medidahm, medidadan, medidadm, medidacm, medidamm))
