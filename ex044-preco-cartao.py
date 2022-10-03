print('\033[33;1m=$='*30)
print('\033[32;1m$$$$$ DESAFIO 44 $$$$$')
print('\033[33;1m=$='*30)

print('\033[31;1m=Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:'
      '\n– à vista dinheiro/cheque: 10% de desconto'
      '\n– à vista no cartão: 5% de desconto'
      '\n– em até 2x no cartão: preço formal '
      '\n– 3x ou mais no cartão: 20% de juros')

print('\033[38;1m')

print('{:▲^40}'.format(' LOJAS AURORA '))
prod = float(input('Qual o valor do produto escolhido: '))
cp = int(input('Qual a forma de pagamento?'
               '\n\033[32;1mA vista Dinheiro/Cheque: 10% desconto. Digite 1.'
               '\n\033[33;1mA vista Cartão: 5% desconto. Digite 2.'
               '\n\033[34;1m2x no cartão. Sem juros. Digite 3.'
               '\n\033[31;1m3x ou mais no cartão. 20% de juros. Digite 4.'
               '\n\033[35;1mQual a opção? '))
if cp == 1:
    print('\033[32;1mO valor de R${:.2f}, vai ficar total de R${:.2f}.'.format(prod, prod - (prod * 10 / 100)))
    print('Obrigado e volte sempre!')
elif cp == 2:
    print('\033[33;1mO valor de R${:.2f}, vai ficar total de R${:.2f}.'.format(prod, prod - (prod * 5 / 100)))
    print('Obrigado e volte sempre!')
elif cp == 3:
    print('\033[34;1mO valor de R${:.2f}, vai ficar total de R${:.2f}.'.format(prod, prod))
    print('Obrigado e volte sempre!')
elif cp == 4:
    print('\033[32;1mO valorde R${:.2f}, cai ficar total de R${:.2f}.'.format(prod, prod + (prod * 20 / 100)))
    print('obrigado e volte sempre!')
else:
    print('obrigado e volte sempre!')

print('')

print('\033[33;1mO homem não teria alcançado o possível se, repetidas vezes, não tivesse tentado o impossível.'
      '\nMax Weber ')

# GUANABARA
print('\033[34;1m')

print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque.
[ 2 ] À vista cartão.
[ 3 ] 2x cartão.
[ 4 ] 3x ou mais no cartão.''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('sua compra de R${:.2f} vai custa R${:.2f} no final.'.format(preço, total))



