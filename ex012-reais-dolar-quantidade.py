print('\033[1;31mCrie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. \033[m')

print('\033[1;36m='*10, 'Desafio 10', '='*10, '\033[m')

rs = float(input('Ola jogador, quantos R$ possui? '))
us = rs / 3.27
print('Jogador possui {:.2f} RS$.\n{} \nCarteira Dolar {:.2f} US$.'.format(rs, '#'*25, us))

# Guanabara

real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
euro = real / 5.25
doleur = dolar / 1.63
print('='*40)
print('Com RS$ \033[1;34m{:.2f}\033[m você pode comprar US$ \033[1;33m{:.2f}\033[m'.format(real, dolar))
print('='*40)
print('Com RS$ \033[1;34m{:.2f}\033[m você pode comprar EU$ \033[1;33m{:.2f}\033[m'.format(real, euro))
print('='*40)
print('Com US$ \033[1;34m{:.2f}\033[m você pode comprar EU$ \033[1;33m{:.2f}\033[m'.format(dolar, doleur))
print('='*40)