import random  # ou "from math import shuffle"

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')
alunolist = [aluno1, aluno2, aluno3, aluno4]
orden_sorteio = random.shuffle(alunolist)
print(f'A ordem de apresentção é: \n1º - {alunolist[0]}\n2º - {alunolist[1]}\n3º - {alunolist[2]}\n4º - {alunolist[3]}')
