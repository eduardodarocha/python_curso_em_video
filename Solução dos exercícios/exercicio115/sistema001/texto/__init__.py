# fo = open("foo.txt", "a+")
# texto = input('DIgite o texto: ')
# idade = input('idade: ')
# fo.write(f'\n{texto:<28}\t\t\t\t{idade} anos')
# textoparaler1 = fo.read()
# print(textoparaler1)
#
# fo.close()

def cadastra():
    print('-' * 42)
    print(f'{"NOVO CADASTRO":^42}')
    print('-' * 42)
    nome = input('Nome: ')
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[0;31mERRO: por favor digite um número inteiro válido!\033[m')
        else:
            break
    ac = open('arquivo_cadastro.txt', 'a')
    ac.write(f'{nome:<36}{idade:} anos\n')
    ac.close()
    print(f'Novo registro de {nome} adicionado.')


def mostra_cadastro():
    print('-' * 45)
    print(f'{"PESSOAS CADASTRADAS":^42}')
    print('-' * 45)
    mc = open('arquivo_cadastro.txt', 'r')
    mostra = mc.read()
    print(mostra)
    mc.close()
