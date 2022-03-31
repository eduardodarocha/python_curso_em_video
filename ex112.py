'''
Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no
desafio 111, temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas
com uma validação de dados para aceitar apenas valores que seja monetários.
Python Exercise 112: Inside the utilitiesCeV package that we created in
challenge 111, we have a module called die. Create a function called
readMoney () which is able to function as the imputed function (), but
with data validation to accept only values that are monetary.'''
from exercicio112.utilidadesCeV import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)