print('\033[34;1m→.→.→.→.→ DESAFIO 75  ←.←.←.←.←')
print('\033[31;1mDesenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:'
      '\nA) Quantas vezes apareceu o valor 9.'
      '\nB) Em que posição foi digitado o primeiro valor 3.'
      '\nC) Quais foram os números pares.')
print('\033[33;1m--'*30)
print('\033[38;1m')
########################################################################################################################
#p = num % 2
num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),  int(input('Digite um número: ')))

print(f'\033[36;1mO números escolhidos foram: {num[0]} {num[1]} {num[2]} {num[3]}')

if 9 in num:
      print(f'\033[35;1mO número 9 apareceu {num.count(9)} vezes.')
else:
      print('\033[31;1mNão existe nenhum valor 9.')
if 3 in num:
      print(f'\033[32;1mO primeiro valor 3 está na posição {num.index(3)+1}ª')
else:
      print('\033[31;1mNão existe nenhum valor 3.')
i = 0
for p in range(0, 4):
      #print(p)
      if num[p] % 2 == 0:
            print(f'\033[33;1mO número {num[p]} é PAR na posição {p+1}ª.')
            i +=1

if i <= 0:
      print('\033[31;1mNão existe números PARES.')

#if num[1] % 2 == 0:
#      print(f'O número {num[1]} é PAR.')
#if num[2] % 2 == 0:
#      print(f'O número {num[2]} é PAR.')
#if num[3] % 2 == 0:
#      print(f'O número {num[3]} é PAR.')

########################################################################################################################

# GUANABARA
print('\033[34;1m--'*30)

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
      print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
      print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
      if n % 2 == 0:
            print(n, end=' ')
