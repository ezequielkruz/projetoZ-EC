print('\033[31;1mNessa aula, vamos aprender como criar estruturas condicionais aninhadas, '
      '\nusando os comandos if.. elif.. else em programas Python. ')

print('\033[35mDISCIPLINA NAO É UM DOM, É UM HABITO. ♥')

print('\033[34mCondiçoes aninhadas '
      '')
print('\033[33m')

'''carro.siga()
se carro.esquerda()
      carro.siga()
      carro.direita()
senao se carro.direita()
      carro.siga()
      carro.esquerdo()
senao
      carro.siga()
      carro.pare() 
      
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

if carro.esquerdo():
      bloco1
elif carro.direita():
      bloco2
elif carro.re():
      bloco3
else:
      bloco4
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=      
'''
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo': # Condição Simples
      print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': # Condição Aninhada
      print('Seu nome é bem popular no Brasil.')
elif nome in ' Ana Claudia Jessica Juliana':
      print('Belo nome feminino.')
else: #condição Composta
      print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
