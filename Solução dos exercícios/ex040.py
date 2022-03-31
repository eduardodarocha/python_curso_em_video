n1 = float(input('Digite a 1ºnota: ').strip())
n2 = float(input('Digite a 2º nota: ').strip())
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média foi {media} e você foi \033[7;31mREPROVADO\033[m')
elif 5 <= media < 7:
    print(f'Sua média foi {media} e você está de \033[7;33mRECUPERAÇÃO\033[m')
elif media >= 7:
    print(f'Sua média foi {media} e você foi \033[7;32mAPROVADO\033[m')