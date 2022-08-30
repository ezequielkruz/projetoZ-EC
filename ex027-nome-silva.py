print('\033[1;31mCrie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.\033[m')

print('\033[34mKKKKK Desafio 25 KKKKK\033[m')

nome = str(input('Qual o seu nome? ')).strip()
print(nome[0:5].upper() == 'SILVA') # errei o cod, tem que usar um operador.
#s = '0' in nome
print('Você tem o nome Silva? {}'.format(nome))

#Guanabara

nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))