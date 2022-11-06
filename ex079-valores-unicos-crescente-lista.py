print('\033[34;1m{:█^80}'.format('.→ DESAFIO 79  ←.'))
print('\033[31;1mCrie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. '
      '\nCaso o número já exista lá dentro, ele não será adicionado. '
      '\nNo final, serão exibidos todos os valores únicos digitados, em ordem crescente.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################

lista = []
# SUGESTAO
# Se  usar a lista no final, tipo retirando os números iguais. copia a lista e compara com a outra para eliminar.

l = 0
while True:
    if l >= 2:
        #print('A')
        for b in lista:
            #print('b',b)
            if lista.count(b) > 1:
                #print('B')
                #print(lista.count(b))
                lista.remove(b)
########################################################################################################################
    if l > 5:
        c = str(input('\033[33;1mQuer continua? [S/N] ')).strip()[0]
        if c in 'Ss':
            print('Continue...')
            l = 0
        else:
            lista.sort()
            print(lista)
            break
########################################################################################################################
    a = int(input('\033[34;1mDigite alguns número: '))
    lista.append(a)
    #print(lista)
    print('\033[33;1m-='*30)
    l += 1
########################################################################################################################


print('\033[35;1mO números que você escolheu são: ', end='')
for c in lista:
    print(f'{c} ', end='- ')



#    if l >= 2:
 #       for num in lista:
  #          print('\033[32m', num)
   #         if num == lista.index(num):
    #            print('A')


        #if c == 0:
         #   print()

#        else:
 #           b = lista[c]
  #          print(a)
   #         print(b)
    #        print(lista)
     #       if b == lista.index(a):
      #          print('FIM')
    #while True:
        #if lista == lista:

########################################################################################################################

# GUANABARA
print('\033[34;1m--'*30)

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')



