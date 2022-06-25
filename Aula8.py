import math # importa toda a biblioteca

num = int(input('Digite um número? '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

from math import sqrt, floor # importa uma função especifica da biblioteca

num = int(input('Digite um número: '))
raiz = sqrt(num) # nao precisa da biblioteca math
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

import random

num = random.random()
print(num)

num = random.randint(1, 10)
print(num)

import emoji
print(emoji.emojize('Ola, mundo :star2: :earth_americas: :thumbs_up:🥰:smile:', language='alias'))




