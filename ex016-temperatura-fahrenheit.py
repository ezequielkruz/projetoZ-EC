print('\033[1;31mEscreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.\033[m')

print('\033[35m!@#$% Desafio 14 !@#$%\033[m')

cel = float(input('Quantos graus esta? °C '))
fah = ((9 * cel) / 5) + 32
print('Temperatura atual {:.2f}°C. Em Fahrenheit {:.2f}°F.'.format(cel, fah))
print('Esta quente? {}'.format(cel > 40))

# Guanabara

c = float(input('Informe a temperatura em °C: '))
f = 9 * c / 5 + 32
print('A temperatura de {:.2f}C° corresponde a {:.2f}°F.'.format(c, f))
