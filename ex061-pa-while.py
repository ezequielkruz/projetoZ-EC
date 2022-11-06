print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 61 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mRefaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, '
      '\nmostrando os 10 primeiros termos da progressão usando a estrutura while.')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('()()()()() PROGRESSÃO ARITMETICA ()()()()()')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = int(input('Qual o termo da PA: '))
decimo = primeiro + (pa - 1) * razao
a = 0
p = 1
while a != decimo:
    a = primeiro + razao
    primeiro = a
    p +=1
    print('\033[33;1mPosição {}ª'.format(p))
    print('\033[34;1m{}'.format(a), '→ ')
print('FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ► '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')

