print('\033[1;31mFaça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\033[m')

print('\033[34m&&&&& Desafio 18 &&&&&\033[m')

import math
ang = int(input('Qual o ângulo: '))
# seno = math.cos(ang) esse cod eu errei
seno = math.sin(math.radians(ang))
# cose = math.tan(ang) esse cod eu errei
cose = math.cos(math.radians(ang))
# tang = math.atan2(seno, cose) esse cod eu errei
tang = math.tan(math.radians(ang))
print('O seno do ângulo: {:.2f} \nO cosseno do ângulo: {:.2f} \nA tangente do ângulo: {:.2f}'.format(seno, cose, tang))

# Guanabara

import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
ê