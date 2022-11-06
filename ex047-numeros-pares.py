print('\033[33;1m=○='*30)
print('\033[32;1m○.○.○.○.○ DESAFIO 47 ○.○.○.○.○')
print('\033[33;1m=○='*30)

print('\033[31;1mCrie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. ')
print('\033[33;1m=○='*30)
print('\033[38;1m')

########################################################################################################################

print('Números PARES')
num = int(input('Digite um número 1 à 50: '))
par = num % 2
if num >= 51:
    print('Você foi alem do infinito...')
elif par == 0:
    print('Esses são númeres PARES')
    for c in range(num, 50, 2):
        print(c)
    print('FIM')
else:
    print('Esses números são IMPARES.')
    for c in range(num, 50, 2):
        print(c)
    print('FIM')

print('\033[33;1m=○='*30)
print('Números PARES')
for c in range(2, 50 , 2):
    print(c)
print('FIM')

########################################################################################################################

print('\033[33;1m=○='*30)
print('\033[35;1mTodas as pessoas deveriam aprender a programar, pois isso ensina a pensar.'
      '\nSteve Jobs – fundador da Apple')

########################################################################################################################

# GUANABARA
print('\033[34;1m○='*40)

for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0: # essa função if ela usa mais processador.
        print(n, end=' ')
print('Acabou')

for n in range(2, 51, 2):
    print('.', end='')
    if n % 2 == 0: # essa função if ela usa mais processador.
        print(n, end=' ')
print('Acabou')

print('\033[35;1mAlgoritmos que exijam menos das maquinas, esse grande desafio do bom PROGRAMADOR.')
print('\033[33;1mPROGRAMADOR faz o mesmo trabalho, dando menos trabalho para computador.')

