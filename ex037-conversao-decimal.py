print('\033[33;1m=-='*30)
print('\033[34;1mABCDEF DESAFIO 37 ABCDEF')
print('\033[33;1m=-='*30)

print('\033[31;1mEscreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a '
      '\nbase de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. ')

num = int(input('\033[33;1mDigite um número inteiro: '))
conv = int(input('Qual a base de conversão? '
                 '\n\033[31;1m1 = Binario.'
                 '\n\033[32;1m2 = Octal.'
                 '\n\033[35;1m3 = Hexadecimal.'
                 '\n\033[33;1m4 = Todos.'))
if conv == 1:
    print('O número digitado foi {}, e seu número BINARIO é \033[31;1m{}.'.format(num, bin(num)))
elif conv == 2:
    print('O número digitado foi {}, e seu número OCTAL é \033[32;1m{}.'.format(num, oct(num)))
elif conv == 3:
    print('O número digitado foi {}, e seu número \033[35;1mHEXADECIMAL é {}.'.format(num, hex(num)))
elif conv == 4:
    print('\n\033[34;1mDECIMAL = {}.'
          '\n\033[31;1mBINARIO = {}.'
          '\n\033[32;1mOCTAL = {}.'
          '\n\033[35;1mHEXADECIMAL = {}.'.format(num, bin(num), oct(num), hex(num)))
else:
    print('Opção invalida.')

# GUANABARA
print('\033[34;1m=+='*30)

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 1 ] onverter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} covertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')

print('\033[35;1mQuando me olho no espelho, tenho orgulho de quem eu sou e de quem estou me tornando.')