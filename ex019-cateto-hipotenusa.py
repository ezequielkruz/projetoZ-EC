print('\033[1;31mFaça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. '
      '\nCalcule e mostre o comprimento da hipotenusa.\033[m')

print('\033[1;34mFFFFF Desafio 17 FFFFF\033[m')


'''from math import hypot
num = float(input('Comprimento do cateto oposto: '))
num2 = float(input('Comprimento do cateto adjacente: '))
hip = hypot(num, num2)
hip2 = (num ** 2 + num2 ** 2) ** (1/2)
print('-+'*10, '\nCateto oposto: {:.2f} \nCateto adjacente: {} \nHipotenusa: {:.2f} \nHiponetusa 2: {:.2f}'.format(num, num2, hip, hip2))'''

# Guanabara

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}.'.format(hi))

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {}.'.format(hi))

