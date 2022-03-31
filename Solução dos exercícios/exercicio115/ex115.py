from exercicio115.sistema001 import menu
from exercicio115.sistema001 import texto

opcao = 0
while True:
    opcao = menu.menuprinc()
    if opcao == 1:
        texto.mostra_cadastro()
    elif opcao == 2:
        texto.cadastra()
    else:
        break
print('-' * 42)
print(f'{"Saindo do sistema... Até logo!":^42}')
print('-' * 42)
