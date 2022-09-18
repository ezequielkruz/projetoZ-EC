print('\033[33;1m○○○○○ AULA 14 ○○○○○')

print('\033[34;1mNessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. '
      '\nPor exemplo:'
      '\n'
      'c=1 while c !=10:'
      '\n'
      'print(c)'
      '\n'
      'c+=1'
      '\n'
      'print(‘Acabou’)')
print()

########################################################################################################################

#enquanto não maça:
#      passo
#pega

#while not maça: # a variavel maça sera Falso se não acha a maça, caso contrario vai usando a variavel.
#      passo
#pega

#while not maça:
#      if terra: # tudo que tiver dentro do bloco ele vai verificar cada itens, ate encontrar a maça.
#            passo
#      if bucaro:
#            pula
#      if moeda:
#            pega
#pega
########################################################################################################################
for c in range(1, 10):
      print(c)
print('fim')
########################################################################################################################
c = 1
while c < 10:
      print(c)
      c += 1
print('Fim')
########################################################################################################################
for c in range(1,5): # O for: ele é limitado, ou seja tem que saber onde começa e onde termina.
      n = int(input('Digite um valor: '))
print('FIM')
########################################################################################################################
n = 1
while n != 0: # (n != 0) essa parte chama se FLAG ou ponto de parada ou condição de parada.
      n = int(input('Digite um valor: '))
print('FIM')
########################################################################################################################
n = 'S'
while n == 'S':
      n = int(input('Digite um valor: '))
      r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')
########################################################################################################################
n = 1
par = impar = 0
while n != 0:
      n = int(input('Digite um valor: '))
      if n != 0:
            if n % 2 == 0:
                  par += 1
            else:
                  impar += 1
print('Você digitou {} número pares e {} números impares!'.format(par, impar))
########################################################################################################################

