print('\033[34;1m{:█^80}'.format('.→ DESAFIO 82  ←.'))
print('\033[31;1mCrie um programa que vai ler vários números e colocar em uma lista. '
      '\nDepois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, '
      '\nrespectivamente. Ao final, mostre o conteúdo das três listas geradas.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################

lista = [] # variavel para armazenar a lista
while True: # loop para ler varias números
      n = int(input('Digite um número: ')) # variavel para receber o número digitado
      lista.append(n) # lista vai receber o número digitado
      c = str(input('Quer continuar? [S/N] ')).strip()[0] # para continuar
      print('\033[34;1m-=' * 30)
      if c in 'Nn': # se acondição nao for digitado corretamente, fica no loop
            break

print('Você digitou esse números: ', end='')
for c in lista: # essa for apenas para deixa o número mais bonito no print()
      print(f'{c:█>5} ', end='')
print()
print('\033[33;1m--'*30)
p = [] # lista do par para ser alimentado
i = [] # lista do impar para ser alimentado
for v in lista: # para verificar cada elemento da lista
      if v % 2 == 0: # para verificar se o número é par.
            p.append(v) # adiciona o número na lista de par
            p.sort() # organiza a lista de par, mas não tem necessidade, caso queira.
      else:
            i.append(v)

print(f'Os valores PARES são: {p}')
print(f'Os valores ÍMPARES são: {i}')

########################################################################################################################

 # GUANABARA
print('\033[33;1m--'*30)

num = list()
pares = list()
impares = list()
while True:
      num.append(int(input('Digite um número: ')))
      resp = str((input('Quer continuar? [S/N] ')))
      if resp in 'Nn':
            break
for i, v in enumerate(num):
      if v % 2 == 0:
            pares.append(v)
      elif v % 2 == 1:
            impares.append(v)
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')



