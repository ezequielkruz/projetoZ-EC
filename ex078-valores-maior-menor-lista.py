print('\033[34;1m{:█^80}'.format('.→ DESAFIO 78  ←.'))
print('\033[31;1mFaça um programa que leia 5 valores numéricos e guarde-os em uma lista. '
      '\nNo final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################

lista = []
maior = menor = 0
for v in range(0, 5): # Eu usei o for porque eu sei o LIMITE, se não soube se usaria o WHILE
      lista.append(int(input('Digite um número: ')))
      #print(lista)
      if v == 0:
            maior = menor = lista[v]
      else:
            if lista[v] > maior:
                  maior = lista[v]
                  #lista.index(v)
            if lista[v] < menor:
                  menor = lista[v]
                  #lista.index(v)

print('Os valores escolhidos foram: ', end='')
for c in lista:
      print(f'\033[34;1m{c}', end=' ')

print(f'\nO MAIOR número é: \033[32;1m{maior} na posição: ', end='')
b = 0
for a in lista:
      #print('\033[31;1m', a)
      if a == maior:
            print(f'{lista.index(maior, b)+1}ª', end='...')
      b += 1

print(f'\n\033[34;1mO MENOR número é: \033[32;1m{menor} na posição: ', end='')
b = 0
for a in lista:
      if a == menor:
            print(f'{lista.index(menor, b)+1}ª', end='...')
      b += 1

print('\nFim do programa.')

########################################################################################################################

# GUANABARA
print('\033[34;1m--'*30)
mai = 0
men = 0
listanum = []
for c in range(0, 5):
      listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
      if c == 0:
            mai = men = listanum[c]
      else:
            if listanum[c] > mai:

                   mai = listanum[c]
                   #print(listanum[c])
            if listanum[c] < men:
                  men = listanum[c]
                  #print(listanum[c])


print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
      if v == mai:
            print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in  enumerate(listanum):
      if v == men:
            print(f'{i}...', end='')
print()










