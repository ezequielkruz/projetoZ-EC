print('\033[33;1m=▲='*30)
print('\033[36;1m▲▲▲▲▲ DESAFIO 42 ▲▲▲▲▲')
print('\033[33;1m=▲='*30)

print('\033[31;1mRefaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:'
      '\n– EQUILÁTERO: todos os lados iguais'
      '\n– ISÓSCELES: dois lados iguais, um diferente'
      '\n– ESCALENO: todos os lados diferentes ')

print('\033[38;1m')

a = float(input('Digite um comprimento: '))
b = float(input('Digite um comprimento: '))
c = float(input('Digite um comprimento: '))
if a < b + c and b < a + c and c < b + c and a == b == c: # Acertei esse aqui.
      print('\033[34;1mOs segmentos / {} + {} + {} / formam um TRIANGULO ▲'.format(a, b, c))
      print('O triangulo forma um EQUILATERO. Lados são iguais.')
elif a < b + c and b < a + c and c < a + b and a == b != c != a and a == c != b != a and b == c != a != b: # a == b and a == c and b == c:
      # Esse eu errei por que se colocar um numero alto 44/4/4, 5/5/9 vai da um triangulo isosceles. colocar um 'and' em vez do 'or', sempre vai da erro.
      # Entao usar um if:  dentro de outro if
      print('\033[33;1mOs segmentos / {} + {} + {} / forma um TRIANGULO ▲ ISOSCELES. Dois lados iguais'.format(a, b, c))
elif a < b + c and b < a + c and c < b + a and a != b != c: # Essa parte errei, falto != a no final de !=c.
      print('\033[36;1mOs segmentos / {} + {} + {} / forma um TRINGULO ▲ ESCALENO. Lados diferentes'.format(a, b, c))

#elif triangulo == 1 and a == b == c:
#      print('O triangulo forma um EQUILATERO. Todos os lados sãao iguais.')
else:
      print('\033[31;1mOs segmentos {} + {} + {} NÃO formam um TRIANGULO.'.format(a, b, c))

print('\033[35;1m')
print('Seja fiel nas pequenas coisas porque é nelas que mora a sua força.'
      '\nMadre Teresa de Calcutá ')

# GUANABARA
print('\033[34;1m')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3  and r3 < r1 + r2: # Um if: esta dentro de outro if: eles são condicoes aninhadas.
      print('Os segmentos acima PODEM FORMAR UM TRIANGULO!', end='')
      if r1 == r2 == r3: #r1 == r2 and r2 == r3:
            print('EQUILATERO!')
      if r1 != r2 != r3 != r1:
            print('ESCALENO!')
      else:
            print('ISOSCELES!')
else:
      print('Os segmentos acima NAO PODEM FORMAR UM TRIANGULO.')

