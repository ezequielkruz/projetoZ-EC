print('\033[33;1m=-='*30)
print('\033[34;1m()()()()() DESAFIO 36 ()()()()()')
print('\033[33;1m=-='*30)
print('\033[31;1mEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa. '
      '\nPergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. '
      '\nA prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')
print('\033[38;1m')
print('Ola amigo, seja bem vindo MCMV, sua corretora de imoveis!')
casa = float(input('\033[32;1mQual o VALOR da casa desejada: R$ '))
salario = float(input('\033[33;1mQual a sua RENDA: R$ '))
ano = int(input('\033[35;1mEm quantos ANOS quer amortiza a casa? '))
ap1 = casa / (ano * 12)
print(ap1)
ap2 = salario * 30 / 100
print(ap2)
print('\033[33;1m=-='*30)
if casa < 80000 or casa > 300000: # se usar 'and' nao vai validar a condicao, tem que usar 'or'.
    print('O minimo para financiar é R$ 80.000,00 e maximo R$300.000,00. Favor refazer simulação.')

#elif casa > 300000:
#    print('O minimo para financiar é R$ 80.000,00 e maximo R$300.000,00 entre 5 a 30 anos. Favor Refazer simulação.')
#    print('B')
elif ano < 5 or ano > 30: # se usar 'and' nao vai validar a condicao, tem que usar 'or'.
    print('O minimo para financiar é entre 5 a 30 anos. Favor refazer simulação.')
#elif ano > 30:
#    print('O minimo para financiar é R$ 80.000,00 e maximo R$300.000,00 entre 5 a 30 anos. Favor Refazer simulação.')
#    print('D')

#elif ano > 5 and ano < 30:
#    print('O minimo de tempo é de 5 a 30 anos. Favor refazer simulação.')
elif ap1 <= ap2:
    print('\033[34;1mPARABENS, você foi aprovado no financimento da sua casa, encaminhe os documento para liberação.')
else:
    print('\033[33;1mFaça uma nova simulação de sua casa com o gerente do banco.')
print('')
print('\033[33;1m=-='*30)
if salario *30 / 100 >= casa / (ano*12):
    print('\033[38;1mSua Renda financia um valor de \033[34;1mR$R${:.2f}\033[38;1m com amortização de \033[34;1m{} meses.\033[38;1m'.format(salario*30/100, ano * 12))
    print('\033[33;1mSeu Financiamento foi aprovado, dirija ao banco mais proximo.')
else:
    print('\033[31;1mFaça uma nova simulação.')

# GUANABARA

print('\033[34;1m')

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos))
print('A prestação sera de R${:.2f}.'.format(prestacao))
#print('COMPARANDO tem que pagar R${:.2f} e o minimo é de R${:.2f}'.format(prestacao, minimo))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
