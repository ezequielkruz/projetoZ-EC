print('\033[33;1m-'*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 71 ←.←.←.←.←')
print('\033[33;1m-'*30)

print('\033[31;1mCrie um programa que simule o funcionamento de um caixa eletrônico. '
      '\nNo início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) '
      '\ne o programa vai informar quantas cédulas de cada valor serão entregues. '
      '\nOBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.')

print('\033[33;1m-'*30)
print('\033[38;1m')

########################################################################################################################

print('\033[33;1m='*30)
print('\033[31;1m         BANCO AURORA')
print('\033[33;1m='*30)
from time import sleep
while True:
    saque = int(input('Qual o valor do saque? R$'))
    sleep(1)
    while saque > 5000:
        print('Você excedeu o limite de saque, tente outro valor.')
        saque = int(input('Qual o valor do saque? R$'))
        sleep(1)
    u = saque // 1 % 10
    d = saque // 10 % 10
    c = saque // 100 % 10
    m = saque // 1000 % 10
    print('Contando seu dinheiro...')
    n50 = 0
    n20 = 0
    n10 = 0
    n1 = 0
    sleep(1)
    if m > 0:
        n50 = m * 20
    if c >= 0:
        n50 = (c * 2) + n50
        print(f'\033[31;1mTotal de {n50:.0f} cédulas de R$50.')
    if d >= 0:
        n20 = d // 2
        print(f'\033[32;1mTotal de {n20:.0f} cédulas de R$20.')
    if d >= 0:
        n10 = d - (n20 * 2)
        print(f'\033[34;1mTotal de {n10:.0f} cédulas de R$10.')
    if u >= 0:
        n1 = u * 1
        print(f'\033[35;1mTotal de {u} cédulas de R$1.')
    sleep(2)
    break
print('\033[33;1m=' * 30)
print('Volte sempre ao BANCO AURORA! Tenha um bom dia!')


#print(f'\n Total de {n20:.0f} cédulas de R$20.')

########################################################################################################################

# GUANABARA
print('\033[34;1m-'*30)

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
#        print(valor, ced, totced) # somente para saber como vai tirando as cédulas
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break

print('=' * 30 )
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


