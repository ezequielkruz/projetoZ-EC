print('\033[1;31mFaça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.\033[m')

print('\033[1;34mVVVVVVVVVVVV DESAFIO 23 VVVVVVVVVV\033[m')

num = str(input('informe 4 número: '))
print('Analisando o número {}:'.format(num))
print('Unidade: {}'.format(num[3:4:].zfill(1)))
print('Dezena: {}'.format(num[2:3:].zfill(1)))
print('Centena: {}'.format(num[1:2:].zfill(1)))
print('Milhar: {}'.format(num[0:1:].zfill(1)))
#print('Unidade: {}'.format(math.num.))

# Guanabara

#   num = int(input('Digite um número: ')) # Se caso ele não digita as 4 unidades vai da ERRO.
#   n = str(num)
#   print('analisando um número: {}'.format(num))
#   print('Unidade {}'.format(n[3]))
#   print('Dezena {}'.format(n[2]))
#   print('Centena {}'.format(n[1]))
#   print('Milhar {}'.format(n[0]))

num = int(input('informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
