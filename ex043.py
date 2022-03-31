print('\033[1;33m🍟🍕🌭🍩🍰🍬🍭🍳' *4)
print('✩✩✩✩  Calculadora de IMC - Índice de massa corporal  ✩✩✩✩')
print('🍟🍕🌭🍩🍰🍬🍭🍳'* 4)
print('\033[m')
peso = float(input('Digite o seu peso em kg: ' ).strip())
altura = float(input('Digite sua altura em metros: ').strip())
imc = peso / (altura ** 2)
print(f'Seu IMC é = {imc:.1f}')
if imc < 18.5:
    print('\033[0;33mVocê está abaixo do peso.\033[m')
elif 18.5 <= imc < 25:
    print('\033[0;32mVocê está com o peso ideal\033[m')
elif 25 <= imc < 30:
    print('\033[1;31mVocê está com sobrepeso.\033[m')
elif 30 <= imc < 40:
    print('\033[1;30;101mVocê está obeso\033[m')
elif imc >= 40:
    print('\033[1;7;97;101mVocê está com obesidade mórbida, procure um médico imediatamente\033[0m')

