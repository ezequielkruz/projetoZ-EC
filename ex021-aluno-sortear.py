print('\033[1;31mUm professor quer sortear um dos seus quatro alunos para apagar o quadro. '
      '\nFaça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.\033[m')

print('\033[1;33m^^^^^ Desafio 19 ^^^^^\033[m')

'''from random import choice
n1 = str(input('Digite primeiro nome: '))
n2 = str(input('Digite segundo nome: '))
n3 = str(input('Digite terceiro nome: '))
n4 = str(input('digite quarto nome: '))
ae = choice(['{}'.format(n1), '{}'.format(n2), '{}'.format(n3), '{}'.format(n4)])
print('Primeiro aluno: {} \nSegundo aluno: {} \nTerceiro aluno: {} \nQuarto aluno: {}'.format(n1, n2, n3, n4))
print('O aluno escolhido é: {}'.format(ae))'''

# Guanabara

import random
a1 = str(input('Primeirp aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido para apagar o quadro foi {}.'.format(escolhido))
