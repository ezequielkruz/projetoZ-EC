print('\033[1;31mDesenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.\033[m')

print('\033[34m===== Desafio 07 =====\033[m')

nt1 = float(input('A nota da primeira prova: '))
nt2 = float(input('A nota da segunda prova: '))
nt3 = float(input('A nota da terceira prova: '))
nt4 = float(input('A nota da quarta prova: '))
nt5 = float(input('A nota da quinta prova: '))
nt6 = float(input('A nota da sexta prova: '))
nt7 = float(input('A nota da setima prova: '))
nt8 = float(input('A nota da oitava prova: '))
nt9 = float(input('A nota da nona prova: '))
nt10 = float(input('A nota da decima prova: '))
nt11 = float(input('A nota da decima primeira prova: '))
nt12 = float(input('A nota da decima segunda prova: '))
nts = nt1 + nt2 + nt3 + nt4 +nt5+nt6+nt7+nt8+nt9+nt10+nt11+nt12
ntm = nts / 4
nta = ntm > 7
print('A soma das provas é: {}\nA média das provas é: {}\nEsta aprovado? {}'.format(nts, ntm, nta))
print(type(nts))
print(type(ntm))
print(type(nta))

# Guanabara

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2 # Ordem de precedencia, senão a conta vai esta errada.
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, média))
