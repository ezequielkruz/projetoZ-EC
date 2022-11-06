print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 58 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mMelhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. '
      '\nSó que agora o jogador vai tentar adivinhar até acertar, '
      '\nmostrando no final quantos palpites foram necessários para vencer....')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('\033[34;1m=I='*10, 'JOGO DE ADVINHAÇÃO', '\033[34;1m=I='*10)
print('\033[33;1mI=I'*30)
j = str(input('A quanto tempo Jogador, vamos jogar? ')).upper()
nj = str(input('Qual seu nome Jogador? ')).upper()
print('\033[36;1m←→'*30)
print('\033[38;1mEstou pensando num número de 0 a 10.')
print('Tente advinhar Jogador, se for capaz...')
import random
cpu = random.randint(0, 10)
print(cpu)
x = 0
while j == 'S':
    print('\033[36;1m←→' * 30)
    j = int(input('\033[34;1mEntre 0 e 10...\nQual número estou pensando... {}? '.format(nj)))
    x += 1
    if j == cpu:
        print('\033[36;1m←→' * 30)
        print('\033[35;1mVocê leu meus pensamentos {}, PARABENS!'
              '\nVocê acerto na {}ª tentativa, nada mal...'.format(nj, x))
    else:
        print('\033[33;1m←→' * 30)
        t = str(input('\033[31;1mVocê não tem capacidade {}, tentar outra vez? '.format(nj))).upper()
        if t == 'S':
            j = 'S'
        else:
            print('\033[33;1mSabia que você não aguentaria a pressão {} ate a próxima. ☺'.format(nj))

print('FIM...')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tenta mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
