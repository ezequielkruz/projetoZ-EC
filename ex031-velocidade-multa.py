print('\033[1;32mIIIII Desafio 29 IIIII')

print('Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo '
      '\nque ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.\033[m')


vel = float(input('Qual a velocidade atual? '))
vl = 80
if vel > vl:
    print('Você ultrapassou o limite de velocidade {} km!'.format(vel))
    print('Sua multa por excesso {:.2f} R$'.format((vel - vl)*7))
else:
    print('PARABENS! esta no limite de velocidade, continue com segurança.')

# Guanabara

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade-80) *7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
