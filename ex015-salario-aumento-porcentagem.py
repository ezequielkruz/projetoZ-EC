print('\033[1;31mFaça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com \033[34m15% de aumento.\033[m')

print('\033[35m$$$$$ Desafio 13 $$$$$\033[m')

sal = float(input('Salário do funcionario: R$ '))
aumento = sal + (sal * 15 / 100)
print('$+'*30)
print('O salário atual é {:.2f}R$. \n{} \nO salário com aumento é {:.2f}R$'.format(sal, '$='*30, aumento))
print('$#'*30)

# Guanabara

salario = float(input('Qual o salario do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novo))
