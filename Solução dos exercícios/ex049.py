# ex049: Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

# ex049: Redo CHALLENGE 009, showing the multiplication table for
# a number that the user chooses, only now using a for loop.

num = int(input('Digite um número para ver a sua tabuada ==> '))
for c in range(1, 11):
    print(f'{num:>2} x {c:>2} = {num * c}')
