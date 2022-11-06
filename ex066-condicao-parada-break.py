print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 66 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mCrie um programa que leia números inteiros pelo teclado. '
      '\nO programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. '
      '\nNo final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('Para desligar o programa digite [999]')
cont = s = 0
while True:
    n = int(input('Digite um número: '))

    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} números, e soma entre eles é {s}')
print('Obrigado e volte sempre!')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont }valores foi {soma}!')
