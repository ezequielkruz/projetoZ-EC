print('\033[34;1m→.→.→.→.→ DESAFIO 76  ←.←.←.←.←')
print('\033[31;1mCrie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. '
      '\nNo final, mostre uma listagem de preços, organizando os dados em forma tabular.')
print('\033[33;1m--'*30)
print('\033[38;1m')
########################################################################################################################

print('-'*60)
print('LISTAGEM DE PREÇOS')
print('-'*60)
lista = ('Lapis', 2.25, 'Borracha', 2, 'Caderno', 12.50, 'Mochila', 80, 'Compasso', 25, 'Canetinha', 18.5,
         'Caneta Bic', 3.5, 'Estojo', 12, 'Caderno Desenho', 35, 'Reguá', 8)
c = 0
while True:
      print(f'{lista[c]:.<50}', end='')

      print(f'R$ {lista[c+1]:5.2f}', end=' ')

      c += 2
      print('\n', end='')
      if c >= len(lista):
            break

print('\n{:+^60}'.format(' PAPELARIA AURORA '))

########################################################################################################################

# GUANABARA
print('\033[34;1m-='*30)

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.3,
            'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
      if pos % 2 == 0:
            print(f'{listagem[pos]:.<30}', end='')
      else:
            print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)


