print('{}Crie um programa que leia dois números e mostre a soma entre eles.{}'.format('\033[1;31m', '\033[m'))
print('\033[33m===== Desafio 03 =====\033[m')
n1 = int(input('Digite um numero? '))
n2 = int(input('Digite um numero? '))
s = n1+n2
print('A soma de {} e {} vale {}'.format(n1, n2, s))

n1 = int(input('Um numero: '))
n2 = int(input('outro numero: '))
s = n1 + n2 * n1
print('a soma de', n1, 'e', n2, 'são', s)

n = input('Digite algo: ')
print(n)
print(type(n))

n = int(input('Digite algo: '))
print(n)
print(type(n))

n = float(input('Digite algo: '))
print(n)
print(type(n))

n = bool(input('Digite algo: '))
print(n)
print(type(n))

n = input('Digite algo: ')
print(n.isnumeric())

