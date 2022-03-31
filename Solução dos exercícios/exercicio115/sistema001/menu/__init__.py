def menuprinc():
    print('-' * 45)
    print(f'{"MENU PRINCIPAL":^45}')
    print('-' * 45)
    print('\033[0;33m1 - \033[0;34mVer pessoas cadastradas')
    print('\033[0;33m2 - \033[0;34mCadastrar nova Pessoa')
    print('\033[0;33m3 - \033[0;34mSair do Sistema\033[m')
    print('-' * 45)
    while True:
        try:
            escolha = int(input('\033[0;32mSua opção: \033[m'))
        except:
            print('ERRO! Digite uma opção válida!')
        else:
            if escolha != 1 and escolha != 2 and escolha != 3:
                print('\033[0;31mERRO! Digite uma opção válida!\033[m')
            else:
                break
    return escolha

