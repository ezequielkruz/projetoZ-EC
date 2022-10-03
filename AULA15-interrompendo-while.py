print('\033[33;1m██████████ AULA 15 ██████████')

print('\033[34;1mNessa aula, vamos aprender como utilizar a instrução break e os loopings infinitos a favor das nossas '
      '\nestratégias de código. É muito importante saber usar o break no Python, '
      '\já que em alguns casos precisamos interromper um laço no meio do caminho. ')

print()

########################################################################################################################

print('Laços de Repetição - parte 3')
print()
'''' enquanto não maça
            se terra
            passo
            se buraco
            pula
            se moeda
            pega
      pega
      
      enquanto
            se terra
            passo
            se buraco
            pula
            se moeda
            pega
            se trofeu
            pela
            interrompa
      pega
      
      while True
            if terra
            passo
            if buraco
            pula
            if moeda
            pega
            if trofeu
            pula
            break
      pega
      
            '''
########################################################################################################################
cont = 1
while cont <= 10:
      print(cont, '→ ', end='')
      cont += 1
print('Acabou')
########################################################################################################################
print('\033[33;1m-1-'*30)
n = 0
while n != 999:
      n = int(input('Digite um número: '))
      cont += 1
########################################################################################################################
print('\033[32;1m-2-'*30)
n = 0
while n < 5:
      n = int(input('Digite um número: '))
      cont += 1
########################################################################################################################
print('\033[31;1m-3-'*30)
n = s = 0
while n != 999:
      n = int(input('Digite um número: '))
      s += n
s -= 999
print('A soma vale {}'.format(s))
########################################################################################################################
print('\033[34;1m-4-'*30)
n = s = 0
while True:
      n = int(input('Digite um número: '))
      if n == 999:
            break
      s += n
print('A soma vale {}'.format(s))
########################################################################################################################
print('\033[33;1m-5-'*30)
n = s = 0
while True:
      n = int(input('Digite um número: '))
      if n == 999:
            break
      s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
########################################################################################################################
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.'%(nome, idade)) # PYTHON 2
########################################################################################################################
nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome:-^} tem {idade} anos e ganha {salario:.2f}')
########################################################################################################################

########################################################################################################################







