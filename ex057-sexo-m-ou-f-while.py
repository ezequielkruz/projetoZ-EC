print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 56 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mFaça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. '
      '\nCaso esteja errado, peça a digitação novamente até ter um valor correto.')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

sexo = 'F'
while sexo == 'M' or sexo == 'F':
      sexo = str(input('Qual seu sexo[M/F]: ')).upper()
      if sexo != 'M' and sexo != 'F':
            print('Não existe esse Genero!')
            m = str(input('Corrigir sua resposta [S/N]? ')).upper()
            if m == 'S':
                  sexo = 'M'
            else:
                  sexo = ''
print('FIM')

########################################################################################################################

# GUANABARA
print('\033[38;1m')

sexo = str(input('Informe seu sexo: [M/F] ')).strip()#.upper()[0]
while sexo not in 'MmFf': # se for digitado essas letras o FLAG é quebrado.
      sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip()#.upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))







