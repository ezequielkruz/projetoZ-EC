print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 69 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mCrie um programa que leia a idade e o sexo de várias pessoas. '
      '\nA cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:'
      '\nA) quantas pessoas tem mais de 18 anos.'
      '\nB) quantos homens foram cadastrados.'
      '\nC) quantas mulheres tem menos de 20 anos. ')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('VVVVV IBGE VVVVV')
i18 = 0
h = 0
m20 = 0
sexo = 'M'
cont = 'S'
while True:
    print('\033[33;1m-=' * 30)
    idade = int(input('Qual é a idade: '))
    sexo = str(input('Qual o genero: [M/F] ')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Qual o genero: [M/F] ')).strip().upper()[0]
    print('Cadastro feito com sucesso!')
    cont = str(input('Quer continuar a cadastrar? [S/N] ')).strip().upper()[0]
    while cont not in 'SsNn':
        cont = str(input('Quer continuar a cadastrar? [S/N] ')).strip().upper()[0]
    if idade > 18:
        i18 += 1
    if sexo in 'Mm':
        h += 1
    if idade < 20 and sexo in 'Ff':
        m20 += 1
    if cont in 'N':
        break
print('\033[34;1m-='*30)
print(f'Existem {i18} maiores de 18 anos.'
      f'\nExistem {h} homens.'
      f'\nExistem {m20} mulheres com menos de 20 anos.')
print('Obrigado pela pesquisa.')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

tot18 = toth = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20 anos')

