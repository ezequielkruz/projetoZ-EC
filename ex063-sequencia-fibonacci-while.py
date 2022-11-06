print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 63 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mEscreva um programa que leia um número N inteiro qualquer e mostre na tela '
      '\nos N primeiros elementos de uma Sequência de Fibonacci. '
      '\nExemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8 ')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('HHHHHHHHHH Sequência de Fibonacci HHHHHHHHHH')

n = int(input('Digite a posição do termo: '))
f = 2
f1 = 0
f2 = 1
if f1 == 0 and f2 == 1:
    print('\033[35;1m{} é {}ª Termo'.format(f1, 1))
    print('\033[35;1m{} é {}ª Termo'.format(f2, 2))
while f < n:
    if f < n:
        f1 += f2
        print('\033[33;1m{} é {}ª Termo'.format(f1, f+1))
        f += 1
    if f < n:
        f2 += f1
        print('\033[34;1m{} é {}ª Termo'.format(f2, f + 1))
        f += 1

print('FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
print('~'*30)
