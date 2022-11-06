print('\033[33;1m=-='*30)
print('\033[36;1mHHHHH DESAFIO 39 HHHHH')
print('\033[33;1m=-='*30)
print('\033[31;1mFaça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, '
      '\nse ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. '
      '\nSeu programa também deverá mostrar o tempo que falta ou que passou do prazo.\033[32;1m')

print('Bem vindo, Soldado! Vamos verificar seu alistamento?')
import datetime
ano = int(input('Em qual ano você nasceu: '))
anoatual = datetime.date.today().year
mesatual = datetime.date.today().month
alistamento = anoatual - ano
print(alistamento)
print(anoatual, mesatual)
if alistamento == 18:
    print('\033[32;1mPARABENS SOLDADO, você ja pode se alistar!'
          'você tem {} mês para se apresentar.'.format(6 - mesatual))
elif alistamento >=19:
    print('PARABENS SOLDADO, você esta bem atrasado no alistamento, acelere seu passo ao quartel. '
          '\n\033[31;1m{} ano e {} meses atrasado.'.format(alistamento - 18, mesatual))
else:
    print('\033[33;1mAinda falta {} anos para se alistar! Esperamos você!.'.format(18 - alistamento))

# GUANABARA
print('\033[34;1m=-='*30)

from datetime import date
atual = date.today().year
gen = str(input('\n[M] Masculino:'
                '\n[F] Feminino:'
                '\nQual seu genero: '))
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18 and gen == 'm':
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and gen == 'm':
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alisatmento sera em {}'.format(ano))
elif idade > 18 and gen == 'm': # Com elif: o programa fica mais visivel do que com else:
    saldo = idade - 18
    print('Você ja deveria ter se alistado ha {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif gen == 'f':
    print('Você não precisa se alistar!')

print()
print('\033[35;1mEu sei que todos os dias quando eu acordo Deus dá um sorriso e me diz: estou te dando a chance de tentar de novo.'
      '\nCaio Fernando Abreu')