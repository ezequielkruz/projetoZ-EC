print('\033[33;1m=+='*30)
print('\033[36;1mAAAAA DESAFIO 41 AAAAA')
print('\033[33;1m=+='*30)

print('\033[31;1mA Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:'
      '\n– Até 9 anos: MIRIM'
      '\n– Até 14 anos: INFANTIL'
      '\n– Até 19 anos: JÚNIOR'
      '\n– Até 25 anos: SÊNIOR'
      '\n– Acima de 25 anos: MASTER')

print('\033[38;1m')
import datetime
print('A Confederação Nacional de Natação, necessita saber qual a sua categoria.')
ano = int(input('Qual o ano do seu nascimento: '))
idade = datetime.date.today().year - ano
print(idade)
if idade > 5 and idade <= 9:
    print('Pela sua idade de {} anos, sua Categoria é \033[32;1mMIRIM!'.format(idade))
elif idade > 9 and idade <= 14:
    print('Pela sua idade de {} anos, sua Categoria é \033[33;1mINFANTIL!'.format(idade))
elif idade > 14 and idade <= 19:
    print('Pela sua idade de {} anos, sua Categoria é \033[34;1mJUNIOR!'.format(idade))
elif idade > 19 and idade <=20:
    print('Pela sua idade de {} anos, sua Categoria é \033[36;1mSENIOR!'.format(idade))
elif idade > 20:
    print('Pela sua idade de {} anos, sua Categoria é \033[31;1mMASTER!'.format(idade))
else:
    print('Você não tem idade para participar!')

print('\033[35;1m')
print('A mídia é uma grande programadora que transforma pessoas em - BOTs - diariamente.'
      '\nAilátaN ')

# GUANABARA
print('\033[34;1m=+='*30)

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')

