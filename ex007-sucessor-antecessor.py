print('{}Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.{}'.format('\033[1;31m', '\033[m'))

print('\033[34m===== Desafio 5 =====\033[m')

n1 = int(input('Digite um número? '))
ns = n1 + 1
na = n1 - 1
print('O sucessor é! {}\nO antecessor é! {}'.format(ns, na))

# Guanabara

n = int(input('Digite um número: '))
a = n - 1 # se caso usar a variavel, guarda na memoria para usar mais pra frente, senão usa atalho
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

# atalho

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'. format(n, (n-1), (n+1)))
