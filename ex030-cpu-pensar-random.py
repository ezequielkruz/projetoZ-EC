print('\033[1;31mEscreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o '
      '\nusuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o '
      '\nusuário venceu ou perdeu.\033[m')

print('\033[34mUUUUU Desafio 28 UUUUU\033[m')

#print('Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário '
#      'tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário '
#      'venceu ou perdeu.')
print('\033[1;33m')
import random
na = random.randint(1, 5)
n = int(input('Qual o número de (0 - 5) que o computador esta pensando? '))
if n == na:
    print('PARABENS! Você leu a mente do computador, uau :), V {} = C {}'.format(n, na))
else:
    print('Você não tem habilidade de programador :(, V {} = C {}'.format(n, na))

# Guanabara
print('\033[1;35m')
from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) # Jogador tenta adivinhar
print('\033[1;30;45mPROCESSSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[1;34mPARABENS! Você conseguiu me vencer!')
else:
    print('\033[1;33mGANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))


