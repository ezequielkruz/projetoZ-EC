print('\033[1;31mO mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. '
      '\nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.\033[m')

print('\033[34m12345 Desafio 20 54321\033[m')

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
s1 = format(lista).split()
random.shuffle(s1) # shuffle = embaralha os objetos.
print('A sequencia de alunos escolhidos é: \n{} '.format(s1))

# Guanabara

import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de aprsentação sera: ')
print(lista)