print('\033[1;33m')
print('QQQQQ Desafio 30 QQQQQ')

print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')

print('\033[m')
n = int(input('Digite um número: '))
u = str(n // 1 % 10)
print(u)
if u == 2:
    print('Seu número {} é PAR.'.format(n))
else:
    print('Seu número {} é IMPAR.'.format(n))

# Guanabara

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
