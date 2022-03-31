from datetime import datetime, date

anonasc = int(input('Que ano o Atleta nasceu: ').strip())
atual = date.today().year
idade = atual - anonasc  # (outra possibilidade)  idade = int(datetime.now().year - anonasc)
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('O atleta esta na categoria \033[1;34mMirin\033[m')
elif 9 < idade <= 14:  # idade <=14
    print('O atleta está na categoria \33[1;34mInfantil\033[m')
elif 14 < idade <= 19:  # idade <=19
    print('O atleta está a categoria \033[1;34mJunior\033[m')
elif 19 < idade <= 25:  # idade <=25
    print('O atleta está na categoria \033[1;34mSênior\033[m')
elif idade > 25:  # else:
    print('O atleta esta na categoria \033[1;34mMaster\033[m')
