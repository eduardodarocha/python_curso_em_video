# ex046: Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

# ex046: Make a program that shows on the screen a countdown
# to the burst of fireworks, going from 10 to 0,
# with a 1 second pause between them.

from time import sleep

print('Contagem regressiva para estouro de fogos de artifício')
for c in range(10, -1, -1):
    print(f'Contagem regressiva ==> {c}')
    sleep(1)
print('🎆 🎆 🎆 🎆 🎆 🎆 Meia noite! Feliz Ano Novo! 🎆 🎆 🎆 🎆 🎆 🎆')
