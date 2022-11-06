print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 67 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mFaça um programa que mostre a tabuada de vários números, um de cada vez, '
      '\npara cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. ')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('\033[32;1m~'*30)
print('\033[33;1mTABUADA LEGAL')
print('\033[32;1m~'*30)

while True:
    print('\033[35;1m-' * 30)
    n = int(input('Qual tabuada você quer ver: '))
    m = 1
    if n < 0:
        break
    while m <= 10:
        print('\033[34;1m-' * 30)
        print(f'{n} x {m:2} = {n*m:2}')
        m += 1

print('Obrigado por multiplicar.')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
