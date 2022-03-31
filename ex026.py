frase = str(input('Digite uma frase: ')).lower().strip()
print(f'A frase tem {frase.count("a")} letras A')
print(f'A primeira letra A fica na posição: {frase.find("a")+1}')
print(f'A última posição da letra A fica na posição {frase.rfind("a")+1}')
