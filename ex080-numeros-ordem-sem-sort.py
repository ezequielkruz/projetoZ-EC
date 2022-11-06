print('\033[34;1m{:█^80}'.format('.→ DESAFIO 80  ←.'))
print('\033[31;1m Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, '
      '\njá na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################
print('ORGANIZANDO SEM USAR SORT()')

lista = []
for c in range(0, 5):
      n = int(input('Digite um número: '))
      if c == 0 or n > lista[-1]:
            lista.append(n)
            print(f'O número foi adicionado na posição {c}...')
#      elif n > lista[len(lista)-1]:
#      elif n > lista[-1]:
#            lista.append(n)
      else:
            pos = 0
            while pos < len(lista):
                  if n <= lista[pos]:
                        lista.insert(pos, n)
                        print(f'O número foi adicionado na posição {pos}...')
                        break
                  pos +=1
print(f'Os números que você escolheu são: {lista}')


##### ERREI TUDO #####
# Acertei uma parte da solução
'''
p = 0
while True:
      n = int(input('Digite um número: '))
      if p == 0:
            lista.append(n)
            print(f'O número foi adcionado a posição {p}')
      else:
            lista.append(n)
            for v in lista:
                  if n == v:

                       # lista.insert(lista.index(n), n)
                        print('lista')
                  else:
                        print('B')

                  print('A')
                  print(v)
                  print(p)
                  print(lista)

      p += 1
      if p > 4:
            break
print(f'O valores que você escolheu foram: {lista}')
'''

'''
cont = 0

while cont < 5:

      num = int(input('Digite um número: '))
      lista.append(num)
      lista_org = []

            cont += 1
tam = len(lista)
for i in range(tam):
      menor = lista[0]
      for j in range(len(lista)):
            if lista[j] < menor:
                  menor = lista[j]
      lista_org.append(menor)
      lista.remove(menor)
      print(lista_org)
print(lista_org)

#if len(lista) > 1:
'''

'''
for c in range(0, 5):
      num = int(input('Digite um número: '))
      lista.append(num)
      #print(lista)
     # print(c)
      if c > 0:
            for l in lista:
                  print('\033[35m{}'.format(l))
                  if num == l:
                        print('\033[34m{}'.format(lista.index(num)))
                        print('\033[33mAdicionado no final da lista...')
                        #print(l)
                        #print(lista)

                  if num > l:
                        print('\033[32mA')

                  if num < l:
                        lista.pop()
                        lista.insert(0, num)
                        print('\033[31mB')
                        print(lista) '''
'''           
      elif c == 1:
            if lista[0] == num:
                  lista.pop()
                  lista.insert(0, num)

                  print('Adicionado na posição 0 da lista...')
            elif lista[0] < num:
                  print('Adicionado no final da lista...')
            elif lista[0] > num:
                  lista.insert(0, num)
                  print('Adicionado no posição 0 da lista...')'''''

########################################################################################################################

#GUANABARA
print('\033[34;1m--'*30)

lista = []
for c in range(0, 5):
      n = int(input('Digite um valor: '))
      if c == 0: # or n > lista[-1]:
            lista.append(n)
            print('Adicionado ao final da lista...')
      elif n > lista[-1]:
            lista.append(n)
            print('Adicionado ao final da lista...')
      else:
            pos = 0
            while pos < len(lista):
                  if n <= lista[pos]:
                          lista.insert(pos, n)
                          print(f'Adicionado na posição {pos}da lista...')
                          break
                  pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram{lista}')
