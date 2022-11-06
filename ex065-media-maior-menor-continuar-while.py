print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 65 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mCrie um programa que leia vários números inteiros pelo teclado. '
      '\nNo final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. '
      '\nO programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('HHHHHHHHHH MEDIAS HHHHHHHHHH')

s = 'S'
m = 0
sn = 0
ma = 0
me = 0
while s == 'S':
    n = int(input('\033[34;1mDigite um número: '))
    m += 1 # Calcula media,  maior e menor
    sn += n # para soma os números
    if m == 1: # indentificar a posiçao
        ma = n
        me = n
    if ma < n: # se o maior for menor que o (n), ele recebe o novo valor digitado.
        ma = n
    if me > n: # se o menor for maior que o (n), ele recebe o novo valor digitado.
        me = n
    s = str(input('\033[32;1mDeseja continuar [S/N]: ')).upper()
    if s != 'S': # IMPORTANTE o if: esta para dentro do WHILE
        media = sn / m
        print('\033[35;1mA soma dos números é {}, e sua média é {:.2f}.'.format(sn, media))
        print('\033[33;1mO maior número é {} e o menor é {}.'.format(ma, me))
        print('\033[32;1m-=' * 30)
        p = str(input('Gostaria de continuar [S/N]: ')).upper()
        if p == 'S':
            s = 'S'
print('\033[34;1mObrigado e volte sempre. FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continua? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
