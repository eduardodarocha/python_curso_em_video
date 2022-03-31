# Exercício Python 097: Faça um programa que tenha uma função
# chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~
# Python Exercise 097: Make a program that has a function
# called write (), that receives any text as a parameter
# and displays a message with an adaptable size.
# Ex:
# write ('Hello, World!')
# Output:
# ~~~~~~~~~~~~
# Hello World!
# ~~~~~~~~~~~~

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

#Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

#Minha solução
# def escreva(palavra):
#     tam = len(palavra) + 4
#     alinhamento = "^"
#     print('~' * tam)
#     print(f'{palavra:{alinhamento}{tam}}')  # ou print(f'{palavra:{"^"}{len(palavra) + 4}}')
#     # ou print(f'{palavra:^{tam}')
#     print('~' * tam)
#
#
# escreva('Curso de Python no Youtube')
# escreva('Gustavo Guanabara')
# escreva('CeV')
# escreva('Olá Mundo!')
