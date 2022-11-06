print('\033[34;1m{:█^80}'.format('.→ DESAFIO 81  ←.'))
print('\033[31;1mCrie um programa que vai ler vários números e colocar em uma lista.'
      '\nDepois disso, mostre:'
      '\nA) Quantos números foram digitados.'
      '\nB) A lista de valores, ordenada de forma decrescente.'
      '\nC) Se o valor 5 foi digitado e está ou não na lista.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################

print('DADOS DA LISTA')

lista = []
cont = 0
while True:
      n = int(input('Digite um número: '))
      lista.append(n)
      cont += 1

      c = ' '
      while c not in 'SsNn':

            c = str(input('Quer continuar: [S/N] ')).strip()[0]
      if c in 'Ss':
            print('\033[33;1m--'*30)

      else:
            print('A')
            break
print('Os números que você escolheu foi: ', end='')
for c in lista:
      print(f' █{c:2}█ ', end='=')
print()
print(f'Foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'sua ordem decrescente é {lista}')

if lista.count(5) >= 1:
      print(f'O número 5 está na lista na posição {lista.index(5)+1}.')
if lista.count(5) == 0:
      print('O número 5 não está na lista.')

########################################################################################################################

#GUANABARA
print('\033[34;1m--'*30)

valores = []
while True:
      valores.append(int(input('Digite um valor: ')))
      resp = str(input('Quer continuar? [S/N] '))
      if resp in 'Nn':
            break
print('-=' * 30 )
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores de ordem decrescente são {valores}')
if 5 in valores:
      print('O valor 5 faz parte da lista!')
else:
      print('O valor 5 não foi encontrado na lista')

