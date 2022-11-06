print('\033[33;1m██████████ AULA 17 ██████████')

print('\033[34;1mNessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. '
      '\nAs listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, '
      '\nacessíveis por chaves individuais.')

print()
########################################################################################################################

#Variaveis compostas (listas)

lanche = ['hamburguer', 'suco', 'pizza', 'pudim'] # uma lista[] para a variavel lanche. MUTAVEL
print(lanche)
########################################################################################################################
lanche[3] = 'picole' # essa função substitui no indice 3
print(lanche)
########################################################################################################################
lanche.append('biscoito') # essa função adciona um elemento na lista no final.
print(lanche)
########################################################################################################################
lanche.insert(0, 'cachorro quente') # essa função coloca uma elemento na posição DESEJADA
print(lanche)
########################################################################################################################
del lanche[3] # essa função deleta um elemento na posição desejada
print(lanche)
########################################################################################################################
lanche.pop(3) # essa função deleta um elemento na posição desejada
print(lanche)
########################################################################################################################
if 'pizza' in lanche: # se caso o elemento não estiver na função remove(), ele vai dar um erro, por isso if:
      lanche.remove('pizza') # essa função deleta um elemento com descrição especifica: string ou int
print(lanche)
########################################################################################################################
lanche.pop() # essa função deleta um elemento na ultima posição
print(lanche)
########################################################################################################################
valores = list(range(4, 11)) # essa função criar elementos dentro da lista
print(valores)
########################################################################################################################
valores = [8, 2, 5, 4, 9, 3, 0] # elementos numa lista
print(valores)
########################################################################################################################
valores.sort() # essa função organiza os elementos
print(valores)
########################################################################################################################
valores.sort(reverse=True) # essa função orgazina os elemntos de forma contraria
print(valores)
########################################################################################################################
len(valores)
print(len(valores)) # essa função conta quantos elementos tem numa lista[]
########################################################################################################################
num = [2, 5, 9, 1]
num[2] = 3
#num[4] = 7
num.append(7) # ADICIONA
print(num)
########################################################################################################################
num.sort() # ORGANIZA
print(num)
########################################################################################################################
num.sort(reverse=True) # ORGANIZA CONTRARIO
print(num)
########################################################################################################################
num.insert(2, 0) # ADICIONA ESPECIFICAMENTE
print(num)
########################################################################################################################
print(f'Essa lista tem {len(num)} elementos.') # QUANTIDADE ELEMENTOS
num.pop() # DELETA ULTIMO ELEMENTO
print(num)
########################################################################################################################
num.pop(2) # DELETA ELEMENTO ESPECIFICO
print(num)
########################################################################################################################
num.insert(2, 2)
print(num)
########################################################################################################################
num.remove(2) # DELETA ELEMENTO DESCRITO(STRING,INT)
if 4 in num:
      num.remove(4)
else:
      print('Não achei o número 4')
print(num)
########################################################################################################################
valores = [] # list() vazia para adicionar elementos
print(valores)
########################################################################################################################
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
########################################################################################################################
for v in valores: # laço da lista []
      print(f'{v}...', end='')
########################################################################################################################
for c, v in enumerate(valores): # essa função c = conta uma posição, v =  recebe o valor de valores, enumerate() = faz o c na sua posiçao
      print(f'\nna posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
########################################################################################################################

valores = list() # outra forma de lista
for cont in range(0, 1):
      valores.append(int(input('Digite um valor: ')))
########################################################################################################################
for c, v in enumerate(valores):
      print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
########################################################################################################################
a = [2, 3, 4, 7]
b = a # essa lista faz uma ligação
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista A: {b}')
########################################################################################################################
b = a[:] # essa lista faz um cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista A: {b}')















