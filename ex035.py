a = float(input('digite o primeiro lado: '))
b = float(input('digite o segundo lado: '))
c = float(input('digite o terceiro lado: '))
# if (abs(b - c)) < a < (c + b):
#     print('O triângulo pode ser formado!')
# else:
#     if (abs(a - c)) < b < (a + c):
#         print('O triângulo pode ser formado!')
#     else:
#         if (abs(a - b)) < c < (a + b):
#             print('o triângulo pode ser formado')
#         else:
#             print('o triangulo não pode ser formado')

if a < b + c and b < a + c and c < a + b:
    print('O triângulo pode ser formado')
else:
    print('O triângulo não pode ser formado')
