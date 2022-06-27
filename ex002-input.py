cor = {'nd':'\033[m',
       'pr':'\033[1;30m',
       'vm':'\033[1;31m',
       'vd':'\033[1;32m',
       'am':'\033[1;33m',
       'az':'\033[1;34m',
       'rx':'\033[1;35m',
       'cl':'\033[1;36m',
       'cz':'\033[1;37m',
       'br':'\033[1;38m'}

print('{}Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas. {}'.format(cor['vm'], cor['nd']))

print('{}===== Desafio 02 ====={}'.format('\033[34m', '\033[m'))
print(cor['am'])
nome = input('qual o seu nome?')
print('prazer em te conhecer, {}!'.format(nome))