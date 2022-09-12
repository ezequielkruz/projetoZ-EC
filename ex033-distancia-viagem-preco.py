print('\033[1;34m')
print('FFFFF Desafio 31 FFFFF')

print('Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,'
      '\ncobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
print('\033[m')

km = float(input('Quantos km tem sua viagem? '))
if km <= 200:
    print('Sua viagem vai custa {:.2f} R$.'.format(km * 0.5))
else:
    print('Sua viagem vai custa {:.2f} R$.'.format(km * 0.45))

# Guanabara

distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagemde {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(preco))

distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagemde {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # Simplificado, eu nao gosto.
print('E o preço da sua passagem sera de R${:.2f}'.format(preco))