print('\033[1;35m')
print('AAAAA Desafio 32 AAAAA')
print('\033[1;32m')
print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
print('\033[m')

ano = int(input('Digite um ano?(ex:1999): '))
bs = ano / 4
print(bs)
if bs == int(ano / 4):
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} não é BISSEXTO.'.format(ano))

import datetime
#from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
a = ano % 4
b = ano % 100
c = ano % 400
print(a, b, c)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
