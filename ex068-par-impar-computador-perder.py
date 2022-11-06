print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 68 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mFaça um programa que jogue par ou ímpar com o computador. '
      '\nO jogo só será interrompido quando o jogador perder, '
      '\nmostrando o total de vitórias consecutivas que ele conquistou no final do jogo. ')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('\033[33;1m=-='*20)
print('█=█=█=█=█ PAR OU IMPAR! █=█=█=█=█')
print('\033[33;1m=-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
from random import randint
pv = 0
while True:
    print('\033[34;1m=-=' * 20)
    j = int(input('Diga um valor: '))
    pi = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print('\033[33;1m---' * 20)
    cpu = randint(1, 5)
    sjc = j + cpu
    v = sjc % 2
    if v == 0:
        print(f'Você jogou {j} e o computador {cpu}. Total de {sjc}, deu PAR.')
        if pi == 'P':
            pv += 1
            print('\033[32;1mVocê VENCEU!'
                  '\nVamos jogar novamente...')
        else:
            print('\033[31;1mVocê PERDEU!')
            break
    else:
        print(f'Você jogou {j} e o computador {cpu}. Total de {sjc}, deu ÍMPAR')
        if pi == 'I':
            pv += 1
            print('\033[32;1mVocê VENCEU!'
                  '\nVamos jogar novamente...')
        else:
            print('\033[31;1mVocê PERDEU!')
            break

print(f'GAME OVER! Você venceu {pv} vezes.')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente.')
print(f'GAME OVER! Você venceu {v} vezes.')


