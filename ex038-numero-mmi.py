print('\033[33;1m=-='*30)
print('\033[35;1mLLLLL DESAFIO 38 LLLLL')
print('\033[33;1m=-='*30)
print('\033[31;1mEscreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:'
      '- O primeiro valor é maior'
      '- O segundo valor é maior'
      '- Não existe valor maior, os dois são iguais'
      '\033[33;1m')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite p segundo número: '))
if n1 > n2:
    print('O primeiro número {} é MAIOR que o segundo {}.'.format(n1, n2))
elif n2 > n1:
    print('O segundo número {} é MAIOR  que o primeiro {}.'.format(n2, n1))
elif n1 == n2:
    print('Não existe número MAIOR, eles são IGUAIS. {} = {}'.format(n1, n2))

# GUANABARA
print('\033[34;1m')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('o SEGUNDO valor é maior.')
else:
    print('Os dois valores são IGUAIS.')

print('\033[34;1m')
print('Se podemos sonhar, também podemos tornar nossos sonhos realidade.'
      '\nWalt Disney')
