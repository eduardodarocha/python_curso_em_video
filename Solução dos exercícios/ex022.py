nome = str(input('Digite o nome: ')).strip()
print('O nome com todas as letras maiúsculas e: {}'.format(nome.upper()))
print(f'O nome em maiúscula é: {nome.upper()}')
print(f'O nome em minúscula é: {nome.lower()}')
print(f'A quant. de caracteres é: {len(nome.replace(" ", ""))}')
lista = nome.split()
print('O primeiro nome é {} e tem {} letras'.format(lista[0], len(lista[0])))
