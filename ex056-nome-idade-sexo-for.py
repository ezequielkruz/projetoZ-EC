print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 56 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mDesenvolva um programa que leia o nome, idade e sexo de 4 pessoas. '
      '\nNo final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e '
      '\nquantas mulheres têm menos de 20 anos.')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################
print('SENSO 2022 - BRASIL')
somaid = 0
#maior = 0
nome1 = 0
fmenor = 0
#print(type(nome1))
for g in range(1, 5):
    nome = str(input('Qual o seu nome: ')).strip().upper()
    idade = int(input('Qual a sua idade: '))
    gen = str(input('Qual seu genero(m/f): ')).strip().upper()
    print(nome, idade, gen)
    somaid += idade
    print(g)
    if g == 1:
        maior = idade
    else:
        if idade > maior:
            maior = idade
            nome1 = nome
    if idade < 20 and gen == 'F':
            fmenor += 1
    print(somaid)
    print(maior)
    print(fmenor)
print('A média de idade do grupo é {}.'.format(somaid / g))
print('{} tem {} anos, é o maior de idade do grupo.'.format(nome1, maior))
print('Existe {} mulheres com menos de 20 anos'.format(fmenor))
#print(type(nome1))

########################################################################################################################

print('\033[35;1m“Bons programadores sabem o que escrever. Os melhores sabem o que reescrever.” '
      '\n– Eric Raymond')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade+= idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm ' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))













