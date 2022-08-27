print('\033[1;31mCrie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.\033[m')

print('\033[32mHHHHH Desafio 24 HHHHH\033[m')

nome = str(input('Qual a cidade que nasceu? '))
s = 'SANTO' in nome
#s = nome.replace('SANTO', 'Tem nome de SANTO')
print('A cidade {} tem nome de santo. {}'.format(nome, s))

# Guanabara

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')