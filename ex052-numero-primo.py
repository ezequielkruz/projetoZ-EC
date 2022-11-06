print('\033[33;1m┼-'*30)
print('\033[34;1m█=█=█=█=█ DESAFIO 52 █=█=█=█=█')
print('\033[33;1m┼='*30)

print('\033[31;1mFaça um programa que leia um número inteiro e diga se ele é ou não um número primo. ')
print('\033[33;1m┼='*30)
print('\033[38;1m')

########################################################################################################################
# 1, 2p, 3p, 4, 5p, 6, 7p, 8, 9, 10, 11p, 12, 13p, 14, 15, 16, 17p, 18, 19p, 20...

print('NÚMEROS PRIMOS')

n = int(input('Digite um número: '))
cp = 0
#np = (n / 1) / n
#print(np)
#np1 = n / n
#np2 = n / 1
#np3 = n / 2
#n1 = n % 2
#n2 = n % 3
#n3 = n % 4
#print(np1, np2, np3, n1, n2, n3)

#if n == 1:
#    print('NÃO É PRIMO {}'.format(n))
#elif n != np1 == 1 and n == np2 and n  np1 :
#    print('NÃO É PRIMO {}'.format(n))
#elif n != np1 and n == np2:
#    print('PRIMO {}'.format(n))
#else: #n == (n / n) and n == (n / 1):
#    print('NÃO É PRIMO {}'.format(n))
#q = 12 % 2
#a = 13 % 2
#z = 14 % 2
#w = 15 % 2
#s = 16 % 2
#x = 17 % 2
#e = 18 % 2
#d = 19 % 2
#c = 20 % 2
#print(q,a,z,w,s,x,e,d,c)
for c in range(2, n):
    if n % c == 0:
        print('Multiplos', cp)
        cp += 1
#    print(c)
if cp == 0 and n >= 2:
    print('\033[34;1mEsse número é PRIMO!')
else:
    print('\033[33;1mNão é número PRIMO!'
          '\nTem {} multiplos acima de 2 e abaixo de {}'.format(cp, n))

########################################################################################################################

print('\033[33;1m=○='*30)
print('\033[35;1mSe você quer ser realmente bom no seu trabalho, '
      '\nvocê tem de ser apaixonado por ele. Se você não dá a mínima para ele, isso vai transparecer.')


########################################################################################################################

# GUANABARA
print('\033[34;1m=○○='*20)

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('\033[33mE por isso ele é PRIMO!')
else:
    print('\033[31mE por isso ele NÃO É PRIMO!')
