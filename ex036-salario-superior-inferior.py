print('\033[1;31m')
print('XXXXX Desafio 34 XXXXX')
print('\033[1;33m')
print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.'
      '\nPara salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.')
print('\033[m')

f1 = float(input('Qual o salario do funcionario: '))
f2 = float(input('Qual o salario do funcionario: '))
if f1 <= 1250:
    print('\033[1;33mEste funcionario tem um aumento de R${:.2f} para R${:.2f}.'.format(f1, (f1 / 100 * 15) + f1))
else:
    print('\033[35mEste funcionario tem um aumento de R${:.2f} para R${:.2f}.'.format(f1, (f1 / 100 * 10) + f1))
if f2 <= 1250:
    print('Este funcionario tem um aumento de R${:.2f} para R${:.2f}.'.format(f2, (f2 / 100 * 15) + f2))
else:
    print('Este funcionario tem um aumento de R${:.2f} para R${:.2f}'.format(f2, (f2 / 100 * 10) + f2))

# Guanabara

salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganha R${:.2f} agora.'.format(salario, novo))
