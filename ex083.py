# Exercício Python 083: Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
# digitada está com os parênteses abertos e fechados na ordem correta.
#
# Python Exercise 083: Create a program where the user types an expression
# whatever that uses parentheses. Your application should analyze whether the
# expression typed has its parentheses open and closed in the correct order.

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão esta errada!')

# Minha solução / Não funciona corretamente
# expres = input('Digite a expressão: ')
# for i in expres:
#     if expres.count('(') == expres.count(')'):
#         print('Sua expressão está valida!')
#         break
#     else:
#         print('Sua expressão não é válida!')
#         break
