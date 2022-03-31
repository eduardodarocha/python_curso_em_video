# ex053: Crie um programa que leia uma frase qualquer e
# diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA,
# A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# ex053: Create a program that reads any sentence and
# say if it is a palindrome, disregarding spaces.
# Examples of palindromes: NEVER ODD OR EVEN, WAS IT A CAT I SAW,
# DO GEESE SEE GOD, LIVE ON TIME EMIT NO EVIL, STEP ON NO PETS.

# frase = input('Digite uma frase: ').strip().lower()
# frase1 = frase.replace(' ','')
# fraseinv = (frase1[::-1])
# if frase1 == fraseinv:
#     print(f'A frase "{frase}" é palíndromo.')
# else:
#     print('A frase não é palindromo')
# # print(fraselist)
# frasecount = len(frase1)
# print(frasecount)

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
# print(f'O invero de {junto} é {inverso}. ')
if inverso == junto:
    print('Isso é um palíndromo')
else:
    print('Isso NÃO é um palíndromo')
