print('\033[34m')

print('Operadores Aritméticos')
n1 = int(input('Um Valor? '))
n2 = int(input('Outro Valor? '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A soma é {},\n o produto é {},\n e a divisão é {}!'.format(s, m, d), end='>>> ')
print('Divisão inteira {},\n potência {}!'.format(di, e))
