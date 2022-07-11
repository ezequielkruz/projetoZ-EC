print('\033[1;31mEscreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.\033[m')

print('\033[35m===== Desafio 08 =====\033[m')

m = float(input('Digite quantos metros: '))
cm = m * 100 # Metros para baixo voce multiplica, metros para cima voce divide, isso vale for para km
mm = m * 1000
print('A metragem de {} em centimetros é {}. \nA metragem de {} em milimetros é {}.'.format(m, cm, m, mm))

# Guanabara

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm.'.format(medida, cm, mm))

# Extra

m = float(input('Uma medida em metros: '))
km = m / 1000
hm = m / 100
dm = m / 10
dc = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {}m corresponde a: \n{} km \n{} hm \n{} dm \n{} dc \n{} cm \n{} mm'.format(m, km, hm, dm, dc, cm, mm))