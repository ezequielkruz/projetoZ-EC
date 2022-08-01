print('\033[31mCrie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.\033[m')

print('\033[33m', '!'*10, 'Desafio 16', '!'*10, '\033[m')

'''from math import trunc
num = float(input('Digite uma fração? '))
print('A fração digitada é {}. O número tem a parte inteira é {}.'.format(num, trunc(num)))'''
# você pode usar ''' ''' para colocar o script todo em comentario, util para usar em teste.

# Guanabara

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))