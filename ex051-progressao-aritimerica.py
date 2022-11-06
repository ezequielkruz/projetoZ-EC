print('\033[33;1m=┼='*30)
print('\033[34;1m█=█=█=█=█ DESAFIO 51 █=█=█=█=█')
print('\033[33;1m=T='*30)

print('\033[31;1mDesenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, '
      '\nmostre os 10 primeiros termos dessa progressão.')
print('\033[33;1m=┼='*30)
print('\033[38;1m')

########################################################################################################################

print('Formula progressão aritmetica: an = a1 + (n - 1) * r ')

s = 0
n1 = int(input('Qual o primeiro termo da P.A.: '))
r = int(input('Qual a razão da P.A.: '))
npa = int(input('Qual a posição P.A.: '))
an = n1 + (npa - 1) * r
#print(an)
for c in range(n1, an+1, r):
    print('\033[33;1m=-=' * 10)
    print('\033[38;1m')
    s += 1
    print('Posição = ', s)
    print('Valor = ', c)
print('\033[32;1m=O=' * 30)
print('FIM')

########################################################################################################################

print('\033[33;1m=○='*30)
print('\033[35;1mSe você quer ser realmente bom no seu trabalho, '
      '\nvocê tem de ser apaixonado por ele. Se você não dá a mínima para ele, isso vai transparecer.')

########################################################################################################################

# GUANABARA
print('\033[34;1m=○○='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='→ ')
print('ACABOU')

