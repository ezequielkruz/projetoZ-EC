print('\033[34;1m→.→.→.→.→ DESAFIO 77  ←.←.←.←.←')
print('\033[31;1mCrie um programa que tenha uma tupla com várias palavras (não usar acentos). '
      '\nDepois disso, você deve mostrar, para cada palavra, quais são as suas vogais.')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################

print('\n\033[34;1m{:=^60}'.format(' VOGAIS TUPLAS '))

palavras = ('Amor', 'Banana', 'Gato', 'Gamer', 'Espaço', 'Torre', 'Guerra', 'Espada', 'Vida', 'Luz', 'Poder',
           'Gelo', 'Chuva', 'Valkirie', 'Aurora', 'Emilly', 'Santo', 'Elemento', 'Programa', 'RPG', 'Deus')

#n = palavras[0]
for p in range(0, len(palavras)): # tirando a palavra da tuplas.
      print(f'\n\033[34;1mA palavra \033[35;1m{palavras[p]}\033[34;1m tem as vogais: \033[33;1m', end='')
      c = palavras[p]
      v = 0
      for a in c:
            #print('\033[34;1m', end='')
            if a in 'Aa':
                  print('a ', end='')
                  v += 1
            if a in 'Ee':
                  print('e ', end='')
                  v += 1
            if a in 'Ii':
                  print('i ', end='')
                  v += 1
            if a in 'Oo':
                  print('o ', end='')
                  v += 1
            if a in 'Uu':
                  print('u ', end='')
                  v += 1
      if v == 0:
            print('\033[31;1mNão tem vogais.', end='\033[38;1m')

print('\n\n\033[36;1mObrigado pelas palavras.')

            #if v in 'Aa':
             #     print(f'{palavras[v].index("a")}', end='')

#print(palavras[0].index('A'))

      #else:
            #print(f'A palavra {palavras[p]} tem as vogais: {palavras[p].count("aA")}')


#print(n.index('m''a'))
#print(n.index('a'))
#print(type(n))

#print(max(palavras[0]))
#print(palavras)

########################################################################################################################

# GUANABARA
print('\033[34;1m--'*30)

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
      print(f'\nNa palavra {p.upper()} temos {".":.<10} ', end='')
      for letra in p:
            if letra.lower() in 'aeiou':
                  print(f'{letra}', end=' ')

