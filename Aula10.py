print('\033[35;1mO usuario é a pior raça que existe :)')

# Condição simples e composta

# if carro.esquerda():
#   bloco True
# else:
#   bloco False

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('---FIM---')

tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo<=3else'carro velho') # Condição simplificada
print('---FIM---')

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!') # Estrutura condicional simple, sem usar o else:
else:
    print('Seu nome é tão normal!') # Estrutura condicional composta, usando o else:
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print('PARABENS' if m>=6 else 'ESTUDE MAIS')
