print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 70 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mExercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. '
      '\nO programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:'
      '\nA) qual é o total gasto na compra.'
      '\nB) quantos produtos custam mais de R$1000.'
      '\nC) qual é o nome do produto mais barato. ')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('\033[33;1m█='*20)
print('█=█=█=█=█ LOJAS AURORA █=█=█=█=█')
print('\033[33;1m█='*20)
print('\033[34;1m')
s = 0
q = 0
c = 0
pb = 0
npb = ''
while True:
    prod = str(input('Nome do \033[33;1mPRODUTO: ')).strip().upper()
    preco = float(input('\033[32;1mPreço: R$'))
    cont = str(input('\033[34;1mQuer continuar? [S/N]')).strip().upper()[0]
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    c += 1
    s += preco
    if preco > 1000:
        q += 1
    if c == 1:
        pb = preco
        npb = prod
    else:
        if pb > preco:
            pb = preco
            npb = prod
    if cont in 'Nn':
        break
print(f'\033[38;1mO total da compra foi '
      f'\033[32;1mR${s:.2f}'
      f'\n\033[38;1mTemos '
      f'\033[33;1m{q}\033[38;1m '
      f'produtos custando mais de R$1000,00.'
      f'\nO produto mais barato foi '
      f'\033[33;1m{npb}\033[38;1m que custa \033[32;1mR${pb:.2f}.')
print('\033[38;1mObrigado e volte sempre. ☺')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

