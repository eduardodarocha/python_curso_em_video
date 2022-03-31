# Exercício Python 114: Crie um código em Python que teste se o site www.pudim.com.br
# está acessível pelo computador usado.
# Python Exercise 114: Create Python code that tests whether the website www.pudim.com.br/
# is accessible by the used computer.

import urllib
import urllib.request
try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print('O site Pudim não esta acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
    print(site.read())


# Minha solução
# import urllib.request
#
# try:
#     teste = urllib.request.urlopen("http://www.pudim.com.br").getcode()
#     print('\n\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
# except:
#     print('\n\033[31mO site Pudim  não esta acessível no momento!\033[m')
