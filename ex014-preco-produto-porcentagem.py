print('\033[1;31mFaça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\033[m')

print('\033[1;32m= = = = = Desafio 12 = = = = =\033[m')

prod = float(input('Qual valor do produto? RS$ '))
desc = (prod / 100) * 5
pd = prod - desc
print('O preço do produto é {:.2f}RS$. \nCom desconto de {:.2f}RS$ fica {:.2f}RS$'.format(prod, desc, pd))
print('Obrigado e volte sempre. :)')

# Guanabara

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava {:.2f}R$, na promoção com desconto de 5% vai custar {:.2f}R$'.format(preco, novo))
