print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 55 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mFaça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('KILOS DA MORTE')
for pess in range(1, 6): # range 0+1 pode ser colocado no format() para indicar posição.
      peso = float(input('Peso da {}ª pessoa? '.format(pess)))
      print(peso)
      if pess == 1:
            p1 = peso
      elif pess == 2:
            p2 = peso
      elif pess == 3:
            p3 = peso
      elif pess == 4:
            p4 = peso
      elif pess == 5:
            p5 = peso
      else:
            print('FIM')
print(p1, p2, p3, p4, p5)
pa = 1
maior = p1
if p2 > p1 and p2 > p3 and p2 > p4 and p2 > p5:
      maior = p2
      pa = 2
elif p3 > p1 and p3 > p2 and p3 > p4 and p3 > p5:
      maior = p3
      pa = 3
elif p4 > p1 and p4 > p2 and p4 > p3 and p4 > p5:
      maior = p4
      pa = 4
elif p5 > p1 and p5 > p2 and p5 > p3 and p5 > p4:
      maior = p5
      pa = 5
menor = p1
pm = 1
if p2 < p1 and p2 < p3 and p2 < p4 and p2 < p5:
      menor = p2
      pm = 2
elif p3 < p1 and p3 < p2 and p3 < p4 and p3 < p5:
      menor = p3
      pm = 3
elif p4 < p1 and p4 < p2 and p4 < p3 and p4 < p5:
      menor = p4
      pm = 4
elif p5 < p1  and p5 < p2 and p5 < p3 and p5 < p4:
      menor = p5
      pm = 5
print('\033[34:1mA {}ª pessoa mais PESADA é {}'.format(pa, maior))
print('\033[33:1mA {}ª pessoa menos PESADA é {}'.format(pm, menor))

########################################################################################################################

print('\033[35;1m “Um dos meus dias mais produtivos foi quando eu joguei fora 1000 linhas de código.” '
      '\n– Ken Thompson ')

########################################################################################################################

# GUANABARA
print('\033[34;1m┼='*30)

maior = 0
menor = 0
for p in range(1, 6):
      peso = float(input('Peso da {}ª pessoa: '.format(p)))
      if p == 1:
            maior = peso
            menor = peso
      else:
            if peso > maior:
                  maior = peso
            if peso < menor:
                  menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
