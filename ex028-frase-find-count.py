print('\033[1;31mFaça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, '
      '\nem que posição ela aparece a primeira vez e em que posição ela aparece a última vez.\033[m')

print('\033[34mTTTTT Desafio 26 TTTTT\033[m')

frase = str(input('Digite uma frase: ')).strip()
print('A letra (a) aparece {} vezes.'.format(frase.upper().count('A')))
print('A letra (a) apareceu primeiro na posição {}.'.format(frase.upper().find('A')))
print('A letra (a) apareceu ultima na posição {}.'.format(frase.upper().rfind('A')))

#Guanabara

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra aparece na posição {}.'.format(frase.find('A')+1))
print('A ultima letra aparece na posição {}.'.format(frase.rfind('A')+1))
