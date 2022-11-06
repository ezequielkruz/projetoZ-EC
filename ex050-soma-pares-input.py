print('\033[33;1m=┼='*30)
print('\033[34;1m█=█=█=█=█ DESAFIO 50 █=█=█=█=█')
print('\033[33;1m=T='*30)

print('\033[31;1mDesenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. '
      '\nSe o valor digitado for ímpar, desconsidere-o.')
print('\033[33;1m=┼='*30)
print('\033[38;1m')

########################################################################################################################

#print('A SOMA está nos PARES!')
#n1 = int(input('O primeiro número: '))
#n2 = int(input('O segundo número: '))
#n3 = int(input('O terceiro número: '))
#n4 = int(input('O quarto número: '))
#n5 = int(input('O quinto número: '))
#n6 = int(input('O sexto número: '))
#print(n1,n2,n3,n4,n5,n6)
s = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    par = num % 2
    if par == 0:
        print('\033[34;1m', num, '\033[m')
        s += num # s = num + s
    else:
        print('\033[33;1m', num, '\033[m')

print('A soma dos números PARES é \033[34;1m▲▼[{}]▼▲'.format(s))

########################################################################################################################

print('\033[33;1m=○='*30)
print('\033[35;1mEscolho uma pessoa preguiçosa para desenvolver um trabalho árduo. '
      '\nPor causa da preguiça, ela vai descobrir um meio simples de resolver o problema.'
      '\nBill Gates')

########################################################################################################################

# GUANABARA
print('\033[34;1m=○○='*20)

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número PARES e a soma foi {}'.format(cont, soma))
