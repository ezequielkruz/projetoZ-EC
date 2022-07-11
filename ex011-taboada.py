print('\033[1;31mFaça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.\033[m')

print('\033[4;33m===== Desafio 09 =====\033[m')

n = int(input('Digite um número: '))
t1 = n * 1
t2 = n * 2
t3 = n * 3
t4 = n * 4
t5 = n * 5
t6 = n * 6
t7 = n * 7
t8 = n * 8
t9 = n * 9
t10 = n * 10
print('O multiplicador de {} na tabuaba é: \n{} x 1 ={}\n{} x 2 ={}\n{} x 3 ={}\n{} x 4 ={}\n{} x 5 ={}\n{} x 6 ={}\n{} x 7 ={}\n{} x 8 ={}\n{} x 9 ={}\n{} x 10 ={}'.format(n, n, t1, n, t2, n, t3, n, t4, n, t5, n, t6, n, t7, n, t8, n, t9, n, t10))

# Guanabara

num = int(input('Digite um número para ver sua taboada: '))
print('='*12)
print('{} x {:2} = {:2}'.format(num, 1, num*1))
print('{} x {:2} = {:2}'.format(num, 2, num*2))
print('{} x {:2} = {:2}'.format(num, 3, num*3))
print('{} x {:2} = {:2}'.format(num, 4, num*4))
print('{} x {:2} = {:2}'.format(num, 5, num*5))
print('{} x {:2} = {:2}'.format(num, 6, num*6))
print('{} x {:2} = {:2}'.format(num, 7, num*7))
print('{} x {:2} = {:2}'.format(num, 8, num*8))
print('{} x {:2} = {:2}'.format(num, 9, num*9))
print('{} x {:2} = {:2}'.format(num, 10, num*10))
print('='*12)
