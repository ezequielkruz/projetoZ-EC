print('\033[34;1m{:█^80}'.format('.→ DESAFIO 83  ←.'))
print('\033[31;1mCrie um programa onde o usuário digite uma expressão qualquer que use parênteses. '
      '\nSeu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e '
      '\nfechados na ordem correta.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################

print('PARÊNTESES')
lista = []
n = str(input('Digite sua expressão: ')).strip().split()
e = ''.join(n)

lista.append(e)
print(lista)
pe = pd = 0

  #          if c[:-1].index('(') > c[:-1].index(')'):
    #              print('AAAAAAA')
     #             pe = 0
for c in lista:
      for l in c:
            print(l)
           # print(c.index('('))
            #print(c.index(')'))
            if l in '(':
                  pe += 1
                  #print('A')
            if l in ')':
                  pd += 1
                  #print('B')
            if l in '()':
                  if c.index('(') > c.index(')'):
                        print('FUD')
                        pe = 0
if pe == pd != 0:
      print(f'A expressão {lista} está CORRETA.')
else:
      print(f'A expressão {lista}, está INCORRETO.')
print('FIM')

'''
if pe == pd:
      print(pe, pd)

      for c in lista:
            for l in c:
                  a = c.index(')')
                  print(c)
                  print(l)
                  if l == '(':

                        pe -= 1
                        print('C')

                  if l == ')':
                        pd -= 1
                        print('D')
print(pe, pd)
# if '(' == ')':
'''

########################################################################################################################

# GUANABARA
print('\033[34;1m--'*30)

expr = str(input('Digite a expressão: ')) # uma variavel para gerar uma expressão
pilha = [] # lista para ser alimentada
for simb in expr: # um laço para verificar meus parenteses() na expressão
      if simb == '(': # condição para adicionar um elemento na lista.
            pilha.append('(') # adicionado elemento ) na lista.
      elif simb == ')': # outra condição para verificar se tem o elemento no laço
            if len(pilha) > 0: # o len() conta quantos elementos tem para pode remove.
                  pilha.pop() # função para remover o ultimo elemento na lista.
            else:
                  pilha.append(')') # adiciona o elemento
                  break
if len(pilha) == 0: # codinção para ver se a expressão é verdadeira ou falsa.
      print('Sua expressão está válida!')
else:
      print('Sua expressão está errada!')

