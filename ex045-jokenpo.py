print('\033[33;1m=♠♦♣='*30)
print('\033[32;1m◘.◘.◘.◘.◘ DESAFIO 44 ◘.◘.◘.◘.◘')
print('\033[33;1m=♠♦♣='*30)

print('\033[31;1mCrie um programa que faça o computador jogar Jokenpô com você.')
print('\033[38;1m')

print('Ola JOGADOR, vamos JOGAR um JOGO? ☻')
print('\033[34;1m◘ J ◘ O ◘ K ◘ E ◘ N ◘ P ◘ Ô ◘')
import random
import time
jog = int(input('\033[35;1mVocê é bom nos dedos JOGADOR?'
                '\n\033[36;1mPEDRA VENCE TESOURA / PAPEL VENCE PEDRA / TESOURA VENCE PAPEL'
                '\n\033[32;1mPEDRA      1'
                '\n\033[38;1mPAPEL      2'
                '\n\033[33;1mTESOURA    3'
                '\n\033[36;1mEscolha sua arma: '))
cpu = random.randint(1, 3)
#p1 = 'PEDRA'
#p2 = 'PAPEL'
#t3 = 'TESOURA'
if jog == 1:
    jog = 'PEDRA'
if jog == 2:
    jog = 'PAPEL'
if jog == 3:
    jog = 'TESOURA'
if cpu == 1:
    cpu = 'PEDRA'
if cpu == 2:
    cpu = 'PAPEL'
if cpu == 3:
    cpu = 'TESOURA'

print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ!')
time.sleep(1)
print()

if jog == cpu:
    print('\033[34;1mJOGADOR = {} '
          '\n\033[35;1mCOMPUTADOR = {}'
          '\n\033[36;1mEMPATAMOS JOGADOR, nada mal...'.format(jog, cpu))
elif jog == 'PEDRA' and cpu == 'TESOURA' or jog == 'PAPEL' and cpu == 'PEDRA' or jog == 'TESOURA' and cpu == 'PAPEL':
    print('\033[34;1mJOGADOR = {} '
          '\n\033[35;1mCOMPUTADOR = {}'
          '\n\033[36;1mJOGADOR GANHOU! sorte...'.format(jog, cpu))
elif jog == 'PEDRA' and cpu == 'PAPEL' or jog == 'PAPEL' and cpu == 'TESOURA' or jog == 'TESOURA' and cpu == 'PEDRA':
    print('\033[34;1mJOGADOR = {} '
          '\n\033[35;1mCOMPUTADOR = {}'
          '\n\033[36;1mJOGADOR PERDEU! muito facil!'.format(jog, cpu))
else:
    print('JOGADA INVÁLIDA')

print('')
print('\033[35;1m“Não é a linguagem de programação que define o programador, mas sim sua lógica.”'
      '\nDavid Ribeiro Guilherme')

# GUANABARA
print('\033[34;1m=♠♦♣='*30)

from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador =  randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))
print('''Sua opções:
[ 0 ]
[ 1 ]
[ 2 ]''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')


