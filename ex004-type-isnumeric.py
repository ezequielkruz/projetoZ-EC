print('{}Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações \n'
      'possíveis sobre ele.{}'.format('\033[1;31m', '\033[m'))

print('\033[33m===== Desafio 04 =====\033[m')

a = input('Digite algo? ')
print('A funçao é? ', type(a))
print('São apenas números?', a.isnumeric())
print('São apenas alfabeticos? ', a.isalpha())
print('São apenas alfanumericos? ', a.isalnum())
print('São apenas espaços? ', a.isspace())
print('São apenas maiusculos? ', a.isupper())
print('São apenas minusculos? ', a.islower())
print('São capitalizados? ', a.istitle())

b = input('Digite uma frase: ')
print('A frase é tipo? ', type(b))
print('tem numeros nas palavras?', b.isnumeric())
print('Tem espaços nas palavras?', b.isspace())
print('Tem alfanumericos nas palavras?', b.isalnum())


