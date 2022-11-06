print('\033[33;1m=▲='*30)
print('\033[36;1m♥♥♥♥♥ DESAFIO 43 ♥♥♥♥♥')
print('\033[33;1m=▲='*30)

print('\033[31;1mDesenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) '
      '\ne mostre seu status, de acordo com a tabela abaixo:'
      '\n– IMC abaixo de 18,5: Abaixo do Peso'
      '\n– Entre 18,5 e 25: Peso Ideal'
      '\n– 25 até 30: Sobrepeso'
      '\n– 30 até 40: Obesidade'
      '\n– Acima de 40: Obesidade Mórbida ')

print('\033[38;1m')

print('Saude o que interessa, o resto nao tem pressa ☻.')
peso = float(input('Qual o seu peso atual: '))
alt = float(input('Qual a sua altura: '))
imc = peso / (alt **2)
print(imc, 'IMC = Peso / Altura².')
if imc < 18.5:
    print('\033[31;1mABAIXO do peso, IMC {:.2f}'
          '\nMelhore sua alimentação ☺'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('\033[34;1mPESO IDEAL, IMC {:.2f}'
          '\nContinue se alimentando bem ☻♥'.format(imc))
elif imc >= 25 and imc < 30:
    print('\033[33;1mSOBREPESO, IMC {:.2f}'
          '\nDiminua consume de carboidratos ☺'.format(imc))
elif imc >= 30 and imc < 40:
    print('\033[31;1mOBESIDADE, IMC {:.2f}'
          '\nMelhore sua alimentação e faça exercicios ☺'.format(imc))
elif imc >= 40:
    print('\033[35;1mOBESIDADE MORBIDA, IMC {:.2f}'
          '\nMelhore sua alimentação, faça exercicios e consulte um nutricionista ☻.'.format(imc))

print('\033[32;1mA persistência é o caminho do êxito.'
      '\nCharles Chaplin ')

# GUANABARA
print('\033[34;1m')

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso/ (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABENS, você esta na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você esta em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você esta em OBESIDADE!')
elif imc >= 40:
    print('Você esta em OBESISADE MORBIDA, cuidado!')
