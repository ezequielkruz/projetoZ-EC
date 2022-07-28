print('\033[1;31mEscreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de '
      '\ndias pelos quais ele foi alugado. \033[33mCalcule o preço a pagar, sabendo que o carro custa R$60 por dia e '
      '\nR$0,15 por Km rodado.\033[m')

print('\033[35m@@@@@ Desafio 15 @@@@@\033[m')

km = float(input('Quantos kilometros foram percorridos? km '))
dia = int(input('Quantos dias alugado? '))
# R$ 60 dia / R$ 0.15 Km
vkm = km * 0.15
vdia = dia * 60
#akm = (km > 100) + km * 5 / 100
tt = vkm + vdia
print('Você rodou {:.2f}km, durante {:.2f} dia. \nValor km: {:.2f}R$ \nValor Dia: {:.2f}R$ \nValor Total {:.2f}R$'.format(km, dia, vkm, vdia, tt))
print('Obrigador por usar Aurora Rent a Car.')

#Guanabara

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O valor total a pagar é de {:.2f}R$'.format(pago))
