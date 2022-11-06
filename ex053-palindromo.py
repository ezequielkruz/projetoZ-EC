print('\033[33;1m┼-'*30)
print('\033[34;1m█=█=█=█=█ DESAFIO 53 █=█=█=█=█')
print('\033[33;1m┼='*30)

print('\033[31;1mCrie um programa que leia uma frase qualquer e diga se ela é um palíndromo, '
      '\ndesconsiderando os espaços. Exemplos de palíndromos:'
      '\nAPOS A SOPA, A SACADA DA CASA, '
      '\nA TORRE DA DERROTA, '
      '\nO LOBO AMA O BOLO, '
      '\nANOTARAM A DATA DA MARATONA..')

print('\033[33;1m┼='*30)
print('\033[38;1m')

########################################################################################################################

print('Z'*20, 'PALINDROMO', 'Z'*20)

#frase = str(input('Digite uma frase: ')).strip().upper()
#print(frase)
#frase = frase.strip()
#a = ''.join(l[::-1] for l in frase.split()) # join se usa para junção das palavras, nesse acaso usando o for
#print(a)
#''.join(frase)
#print(a)

a = ""
frase = str(input('Digite uma frase: ')) #A função input retorna sempre uma string
print(' Você digitou: {}'.format(frase))
a = a.split() # errei
''.join(a) # errei
for palavra in frase[::-1]: #.split(" "): # ('') caso tire o espaço a frase se junta.
    a += palavra[::-1]+""
    print(palavra)
print('A frase que você digitou invertida fica: {}'.format(a))

if frase == a:
    print('\033[34;1mEssa Frase é PALIDROMO')
    print('Sua frase tem {} letras'.format(len(a) - frase.count(' ')))
else:
    print('\033[33;1mEssa frase invertida é assim:\n{}'.format(a))



#if frase ==
########################################################################################################################
# Como fazer uma String invertida.
#new_string = ""
#frase = input('Digite uma frase: ') #A função input retorna sempre uma string
#print(' Você digitou: {}'.format(frase))
#for palavra in frase.split(" "): # ('') caso tire o espaço a frase se junta.
#    new_string += palavra[::-1]+" "
#print('A frase que você digitou invertida fica: {}'.format(new_string))

########################################################################################################################

# GUANABARA
print('\033[34;1m=○○='*20)

frase = str(input('Digite uma frase: ')).strip().upper() # strip() elemina espaços, upper() coloca a frase em maiusculo.
palavras = frase.split() # split() coloca a frase numa lista em forma de palavras.
junto = ''.join(palavras) # ''.join() junta as palavras sem espaço(caso queira) dentro da frase.
#############################################################

#inverso = junto[::-1] # opção extra para usar invertido a frase, sem usar o for:

#############################################################
inverso = '' # essa variavel serve para usar no for: para ser preenchida com uma string.
for letra in range(len(junto) -1, -1, -1): # esse for: serve para inverte a frase dentro de uma variavel.
    inverso += junto[letra] # aqui você soma as letras retiradas do for: para a variavel inverso.
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto: # aqui você confirma True se as variaveis tem a mesma string ou valor.
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')


