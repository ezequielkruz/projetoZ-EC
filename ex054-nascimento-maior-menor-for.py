print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 54 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[3;1mCrie um programa que leia o ano de nascimento de sete pessoas. No final, '
      '\nmostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('SELEÇÃO DE IDADES!')

import datetime
id1 = 0
id2 = 0
for ano in range(0, 8):
    nasc = int(input('Qual o ano do seu nascimento: '))
    idade = datetime.date.today().year - nasc
    if idade < 21:
        id1 += 1
    else:
        id2 += 1
#    print(idade)
#    print(ano)
print('\033[34;1mMenores de 21 temos {} pessoas'
      '\n\033[33:1mMaiores de 21 temos {} pessoas'.format(id1, id2))

########################################################################################################################

print('\033[35;1m"Sou só um vírus, querendo escapar, dos programadores da vida."'
      '\nWesley D`Amico')

########################################################################################################################

# GUANABARA
print('\033[34;1m┼='*30)

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))