def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha()or entrada == '':
            print(f'\033[1;31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)




# Minha solução
# def leiaDinheiro(valor):
#     preco = input(valor)
#     while True:
#         preco = preco.strip()
#         preco = preco.replace(',', '.')
#         if preco.isalpha() or preco == '':
#             print(f'\033[1;31mERRO! "{preco}" é um preço inválido!\033[m')
#             preco = input('Digite um preco3: R$')
#         else:
#             return float(preco)


#p = leiaDinheiro('Digite um preço: R$')
