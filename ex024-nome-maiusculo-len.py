print('\033[1;31mCrie um programa que leia o nome completo de uma pessoa e mostre:'
      '\n\033[1;33m– O nome com todas as letras maiúsculas e minúsculas.'
      '\n\033[1;34m– Quantas letras ao todo (sem considerar espaços).'
      '\n\033[1;35m– Quantas letras tem o primeiro nome.\033[m')

print('\033[32m()()() Desafio 22 ()()()\033[m')

nome = str(input('Digite seu nome completo: '))
print('Seu nome completo em maiusculo : {}'.format(nome.upper()))
print('Seu nome completo em minusculo: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome))) # Aqui errei
primeiro = nome.split()
print('Seu nome completo tem {} letras.'.format(len(primeiro[0:])))
print('Seu primeiro nome tem {} letras.'.format(len(primeiro[0])))

# Guanabara

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome[0:10].upper()))
print('Seu nome em minúsculs é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
print('Seu primeiro nome maiusculo: {}'.format(separa[0].upper()))
print('Seu nome completo titular: {}'.format(separa[0].title))