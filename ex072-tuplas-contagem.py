print('\033[34;1m→.→.→.→.→ DESAFIO 72 ←.←.←.←.←')
print('\033[31;1mCrie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. '
      '\nSeu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.')
print('\033[33;1m--'*30)
print('\033[38;1m')
########################################################################################################################
# USANDO UM METODO

#import num2words
#ne = int(input('Digite um número de 0 a 20: '))
#numtx = num2words.num2words(ne, lang='pt-br')
#print(f'Você digitou {numtx}')

# USANDO TUPLAS

while True:
      n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze','quatorze', 'quinze', 'dezesseis', 'dezesseta', 'dezoito', 'dezenove', 'vinte')
      c = ''
      while c not in range(0, 21):
            c = int(input('Digite um número de 0 à 20: '))
      n = n[c]
      break
print(f'Você digitou {n}')

########################################################################################################################

# GUANABARA

cont = ('zero', ' um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenova', 'vint')
while True:
      num = int(input('Digite um número entre 0 e 20: '))
      if 0 <= num <= 20:
            break
      print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[num]}')
