cidade = input('Digite o nome da cidade: ').strip()
nome = (cidade[:6].lower())
nomesanto = 'santo ' == nome
print('A cidade começa com a palavra Santo: {} {}'.format(('santo ' in nome), (nomesanto)))

# cidade = input('Digite o nome da cidade: ').strip()
# nome = (cidade[:6].lower())
# nomesanto = 'santo' in nome
# print('A cidade começa com a palavra Santo: {}'.format(nomesanto))
