print('\033[33;1m=T='*30)
print('\033[34;1mS=S=S=S=S DESAFIO 49 S=S=S=S=S')
print('\033[33;1m=T='*30)

print('\033[31;1mRefaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, '
      '\nsó que agora utilizando um laço for..')
print('\033[33;1m=○='*30)
print('\033[38;1m')

########################################################################################################################

print('\033[32;1m/*-+'*20)
print('▲'*30,  'A TABOADA INSTINTO SUPERIOR', '▲'*30)
print('\033[32;1m/*-+'*20)
print('\033[33;1m')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o limite do multiplicador: '))
print('\033[32;1m▼'*30)
for c in range(0, n2+1):
    print('{:4} X {:4} = {:4}'.format(n1, c, c * n1))
print('\033[32;1m▲'*30)

########################################################################################################################

print('\033[33;1m=○='*30)
print('\033[35;1mOs líderes do futuro são os que empoderam os outros.'
      '\nBill Gates')

########################################################################################################################

# GUANABARA
print('\033[34;1m=○○='*20)

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
