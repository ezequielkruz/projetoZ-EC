print('\033[33;1m=-='*30)
print('\033[36;1mDDDDD DESAFIO 40 DDDDD')
print('\033[33;1m=-='*30)

print('\033[31;1mCrie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:'
      '\n– Média abaixo de 5.0: REPROVADO'
      '\n– Média entre 5.0 e 6.9: RECUPERAÇÃO'
      '\n– Média 7.0 ou superior: APROVADO')

print('\033[38;1m')
n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('\033[31;1mVocê foi REPROVADO! Sua media foi {:.1f}'.format(media))
elif media >= 5 and media <=6.9:
    print('\033[33;1mVocê fico de RECUPERAÇÃO! Sua media foi {:.1f}'.format(media))
elif media >= 7:
    print('\033[34;1mPARABENS! Você passou. Sua media foi {:.1f}'.format(media))

print('\033[35;1m=+='*30)
print('\033[38;1mFaça como um programador. Quando tudo está errado e confuso, apague tudo e recomece do zero.'
      '\nOrlando Cordeiro ')

# GUANABARA
print('\033[34;1m=+='*30)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if media >= 5 and media < 7: # 7 > media >= 5:
    print('O aluno esta em RECUPERACAO.')
elif media < 5:
    print('O aluno esta REPROVADO.')
elif media >= 7:
    print('O aluno esta APROVADO.')
