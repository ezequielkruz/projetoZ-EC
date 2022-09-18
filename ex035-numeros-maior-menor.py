print('\033[1;36m')
print('YYYYY Desafio 33 YYYYY')
print('\033[1;31m')
print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
print('\033[m')

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
sorted([n1, n2, n3])    # Eu errei aqui
print(sorted([n1, n2, n3]))
if sorted([n1, n2, n3]):    # Eu errei aqui
    print('O número {} é MAIOR.'.format(sorted([3]))) # Eu errei aqui
else:

    print('O número {} é MENOR'.format(n1 == n1 < n2 < n3))

if n2 > n1 > n3: # Eu errei aqui
    print('O número {} é MAIOR.'.format(n2))
else:
    n2 < n1 < n3
    print('O número {} é MENOR'.format(n2))
if n3 > n2 > n1:
    print('O número {} é MAIOR.'.format(n3))
else:
    n3 < n2 < n1
    print('O número {} é MENOR'.format(n3))

# Guanabara

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Menor número / outra maneira de escrever o cod.
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print('O MENOR número dos 3 é: {})'.format(menor))
# Verificar quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificar quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))





