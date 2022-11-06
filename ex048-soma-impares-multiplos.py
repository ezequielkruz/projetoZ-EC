print('\033[33;1m=○='*30)
print('\033[32;1m○.○.○.○.○ DESAFIO 48 ○.○.○.○.○')
print('\033[33;1m=○='*30)

print('\033[31;1mFaça um programa que calcule a soma entre todos os números que são múltiplos de três '
      '\ne que se encontram no intervalo de 1 até 500.')
print('\033[33;1m=○='*30)
print('\033[38;1m')

########################################################################################################################

s = 0
n = int(input('Digite um número: '))
print('Números IMPARES')
for c in range(1, n, 2):
    d = c % 3
    if d == 0:
        s += c # s = s + c
        print('\033[34m', c)
    else:
        print('\033[33m', c)
print('\033[38;1mA soma dos números multiplos de 3 são \033[34;1m▲[{}]▲'.format(s))

########################################################################################################################

print('\033[33;1m=○='*30)
print('\033[35;1mAprender a programar aumenta a mente, ajuda a pensar melhor.'
      '\nBill Gates – Fundador da Microsoft')

########################################################################################################################

# GUANABARA
print('\033[34;1m=○○='*20)

soma = 0 # ele acumula/soma os valores dentro do for:
cont = 0 # ele conta/soma cada vez que ele acha um valor pedido.
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += +1 # cont = cont + 1
        soma += c # soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))