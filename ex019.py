import random

aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')
aluno_list = [aluno1, aluno2, aluno3, aluno4]
sorteada = random.choice(aluno_list)
print('O aluno sorteado foi', sorteada)
