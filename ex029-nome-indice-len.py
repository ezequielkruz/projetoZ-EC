print('\033[1;31mFaça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o '
      '\núltimo nome separadamente.\033[m')

print('\033[34mRRRRR Desafio 27 RRRRR\033[m')

nome = str(input('Qual é o seu nome: ')).strip().split() # Se tiver uma apresentacao bom usar spli() num objeto.
print(nome)
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[-1]))

#Guanabara

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu ultimo nome é {}.'.format(nome[len(nome)-1]))
