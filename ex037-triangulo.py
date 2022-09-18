print('\033[1;34m')
print('ZZZZZ Desafio 35 ZZZZZ')
print('\033[1;33m')
print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um '
      'triângulo.')
print('\033[m')
a = int(input('Digite um comprimento: '))
b = int(input('Digite um comprimento: '))
c = int(input('Digite um comprimento: '))
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('Esses comprimento {}, {} e {} FAZ um Triangulo ▲'.format(a, b, c))
else:
    print('Esses comprimentos {}, {} e {} NAO FAZ um Triangulo ▲'.format(a, b, c))


# Guanabara

print('\033[1;34m')
print('-=-'*20)
print('Analisador de Triângulo ▲')
print('-=-'*20)
print('\033[m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR TRIANGULO.')
else:
    print('Os segmentos acima NAO PODEM FORMAR TRIANGULO.')



