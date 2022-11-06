print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 59 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mMENU...')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

from time import sleep
print('\033[34;1m-='*10, 'MENU DE CALCULAR', '\033[34;1m-='*10)

m = 0
while m == 0:
    print('\033[34;1m→.←'*20)
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    opc = int(input('\033[33;1mO que gostaria de fazer com os valores?'
                    '\n[1] SOMAR'
                    '\n[2] MULTIPLICAR'
                    '\n[3] MAIOR'
                    '\n[4] NOVOS NÚMEROS'
                    '\n[5] SAIR DO PROGRAMA'
                    '\n█→ '))
    if opc == 1:
        print('\033[32;1mA soma de {} e {} são {}.'.format(n1, n2, n1+n2))
    if opc == 2:
        print('\033[35;1mA mulpiplicação de {} e {} são {}.'.format(n1, n2, n1*n2))
    if opc == 3:
        if n1 > n2:
            print('\033[36;1mO {} é MAIOR que {}.'.format(n1, n2))
        elif n1 < n2:
            print('\033[36;1mO {} é MAIOR que {}.'.format(n2, n1))
        else:
            print('\033[36;1mOs valores {} e {} são iguais.'.format(n1, n2))
    if opc == 4:
        m = 0
    if opc == 5:
        print('Obrigado e volte!')
        m = 1
sleep(.5)
print('SISTEMA DESLIGANDO...')
for c in range(3, -1, -1):
    print(c)
    sleep(1)
print('FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10 )
    sleep(3)
print('Fim do programa! Volte sempre!')


