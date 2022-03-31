nome = input('Digite o o nome: ').strip()
lista = nome.split()
print(f'O 1º nome é = {lista[0]}')
lista1 = lista[::-1]
print(f'O último nome é = {lista1[0]}')
print(f'O último nome é = {lista[-1]}')  #alternativa ao comando anterior


