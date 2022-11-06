print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 60 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mFaça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:'
      '\n5! = 5 x 4 x 3 x 2 x 1 = 120')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('()()()()() NÚMERO FACTORIAL ()()()()()')
import math
n = 0
#while n == 0:
#    f = int(input('Digite um número: '))
#    nf = math.factorial(f)
#    print(nf)
#    n = 1
#print('FIM')
f = int(input('Digite um número: '))
n = f
n1 = f
f1 = f
if f == 0:
    f = 1
    n = 1
    n1 = 0

while f != 1:
        n = n * (f - 1) # Para achar seu multiplicador, multiplique seu número pela posição(f) com menos (-1)
        f -= 1
        n1 -= 1
        print('\033[33;1m{}! = {} * '.format(f1, n1), n)
#    n = ft * (n - 1) # ERRADO
#    n -= 1 # ERRADO
print('\n\033[34;1mO FATORIAL de {}! é {} na posição {}ª'.format(f1, n, f))
print('FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n, end=''))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
#    print('{}'.format(f))
print('{}'.format(f))
