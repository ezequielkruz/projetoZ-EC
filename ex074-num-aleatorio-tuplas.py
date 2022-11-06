print('\033[34;1m→.→.→.→.→ DESAFIO 74  ←.←.←.←.←')
print('\033[31;1mCrie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. '
      '\nDepois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.')
print('\033[33;1m--'*30)
print('\033[38;1m')
########################################################################################################################

import random

tuplas = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
t = ma = me = 0
print(f'Os valores sorteados foram: ', end='')
while t < 5:
    ta = tuplas.index(random.randint(0, 9))
    t += 1
    print(ta, end=' ')
    if t == 1:
        ma = me = ta
    else:
        if ta > ma:
            ma = ta
        if ta < me:
            me = ta
print(f'\n\033[33;1mO maior número das tuplas é {ma}'
      f'\nO menor número das tuplas é {me}')

#a = tuplas.index(random.randint(0, 9))
#b = tuplas.index(random.randint(0, 9))
#c = tuplas.index(random.randint(0, 9))
#d = tuplas.index(random.randint(0, 9))
#e = tuplas.index(random.randint(0, 9))
#print(f'Os valores sorteados foram: {a}{b}{c}{d}{e}')
print('FIM')

#ale = random.randint(b, a)
#print(ale)

########################################################################################################################

# GUANABARA
print('\033[34;1m-=' * 30)

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('O valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f' \nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

