# Exercício Python 077: Crie um programa que tenha uma tupla
# com várias palavras (não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.
# Python Exercise 077: Create a program that has a tuple
# with multiple words (do not use accents). After that, you
# must show, for each word, what its vowels are.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar','trabalhar',
            'mercado', 'programador', 'futuro', 'individuais',
            'reeducação', 'exercises', 'subdirectory')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end ='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



#Minha solução
# palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar','trabalhar',
#             'mercado', 'programador', 'futuro', 'individuais', 'reeducação', 'exercises', 'subdirectory')
# cont = 0
# lista = ''
# tamanho = len(palavras)
# while cont < tamanho:
#     cont1 = 0
#     lista = ''
#     verifpalavra = palavras[cont]
#     tam = len(verifpalavra)
#     while cont1 < tam:
#         if 'a' in verifpalavra[cont1]:
#             lista = lista + 'a '
#         elif 'e' in verifpalavra[cont1]:
#             lista = lista + 'e '
#         elif 'i' in verifpalavra[cont1]:
#             lista = lista + 'i '
#         elif 'o' in verifpalavra[cont1]:
#             lista = lista + 'o '
#         elif 'u' in verifpalavra[cont1]:
#             lista = lista + 'u '
#         cont1 += 1
#     print(f'Na palavra {verifpalavra.upper()} temos {lista}')
#     cont += 1
