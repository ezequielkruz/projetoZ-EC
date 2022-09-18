print('○○○○○ AULA 13 ○○○○○')

print('\033[31;1mNessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, '
      '\nque é uma estrutura versátil e simples de entender. Por exemplo:'
      '\nfor c in range(0, 4):'
      '\nprint(c)'
      '\nprint(‘Acabou’)')

print('\033[35mClientes'
      '\nVocê quer isso rápido, barato, ou bem feito? Você pode escolher duas das três. ☺')

print('for são estruturas de repetição')

#c = 1
#for c in range(0, 10): # Não esquece os dois ponto: for = laço / c = varialvel / in = no / range()= intervalo()
#      passo
#      pega
#passo
#pega

#for c in range(0, 3):
#      if moeda
#            pega
#      passo
#      pega
#passo
#pega
print('\033[33;1m=○='*30)

for c in range(0, 6): # o ultimo número ele ignora, no caso so ia ler ate 5
      print(c)
print('FIM')

print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')

print('\033[33;1m=○='*30) ###########################################################################################

for c in range(0, 6): # usando o for para repetir a string
      print('oi')
print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

for c in range(0, 6): # atenção na posição identação
      print('oi')
      print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

for c in range(0, 6): # o ultimo número ele ignora, no caso so ia ler ate 5
      print(c)
print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

for c in range(6, 0, -1): # nesse caso o -1 faz ler ao contrario.
      print(c)
print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

for c in range(0, 7, 2): # nesse caso o 2 pula o número.
      print(c)
print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

n = int(input('Digite um número: ')) # o número digitado vai determinar onde vai termina a contagem.
for c in range(0, n+1):
      print(c)
print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): # nesse caso você esta colocando os valores em cada situação
      print(c)
print('FIM')

print('\033[33;1m=○='*30) ###########################################################################################

for c in range(0, 3): # aqui ele vai pedir para digitar 3x o número.
      n = int(input('Digite um valor: '))
print('fim')

print('\033[33;1m=○='*30) ###########################################################################################

s = 0
for c in range(0, 4): # aqui ele vai pedir para digitar 4x o número e somar todos que foram digitado.
      n = int(input('Digite um valor: ')) # Fabianamattossamapio
      s += n # s = s + n

print('O somatório de todos os valores foi {}.'.format(s))






