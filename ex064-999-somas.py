print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 64 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mCrie um programa que leia vários números inteiros pelo teclado. '
      '\nO programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. '
      '\nNo final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('HHHHHHHHHH 999 HHHHHHHHHH')

print('\033[34;1mVamos somar seus números até vc chega em 999.')
soma = 0
n = 0
c = 0
while n != 999:
    n = int(input('\033[34;1mDigite um número: '))
    c += 1
#    soma += n
#    print('\033[33;1mA soma dos números é {}'.format(soma))
    if n != 999:
        soma += n
        print('\033[33;1mA soma dos números é {}'.format(soma))
    if n == 999:
        soma = (soma + n) - n # se usar 999 na subtração também da o mesmo resultado.
        print('\033[33;1mA soma dos números é {} e foram digitados {} números'.format(soma, c))
print('FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entres eles foi {}.'.format(cont, soma))

