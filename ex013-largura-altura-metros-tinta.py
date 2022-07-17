print('\033[1;36;40mFaça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a \033[m'
      '\n\033[7;38;42mquantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.\033[m')

print('\033[35m', '='*10, 'Desafio 11', '='*10, '\033[m')

l = float(input('Qual a largura? m '))
a = float(input('Qual a altura? m '))
area = l * a
tinta = area / 2
perda = (tinta / 100) * 5
tt = tinta + perda
print('A area total é: {:.2f} m2. \nTotal de tinta: {:.2f} lt.'.format(area, tt))

# Guanabara

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {:.2f}lt de tinta.'.format(tinta))
