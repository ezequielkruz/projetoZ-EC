print('\033[34;1m→.→.→.→.→ DESAFIO 73  ←.←.←.←.←')
print('\033[31;1mCrie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, '
      '\nna ordem de colocação. Depois mostre:'
      '\na) Os 5 primeiros times.'
      '\nb) Os últimos 4 colocados.'
      '\nc) Times em ordem alfabética.')

print('\033[33;1m--'*30)
print('\033[38;1m')
########################################################################################################################
print('{:=^60}'.format(' CAMPEONATO BRASILEIRO '))

time = ('Corinthians', 'Palmeiras', 'Atletico-PR', 'Atlético-MG', 'Coritiba',
        'São Paulo', 'Internacional', 'Fluminense', 'América-MG', 'Santos',
        'Bragantino', 'Ceará', 'Goiás', 'Flamengo', 'Botagofo',
        'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude', 'Fortaleza')
#print('{:º█º^4}'.format(time)) # não aceita formatar
j = int(input('[1] 5 primeiros do Brasileirão.'
              '\n[2] 4 útimos do Brasileirão'
              '\n[3] Time em ordem Alfabética'
              '\n[4] posição do preferido.'
              '\nQual opção: '))
if j == 1:
    print(time[0:5])
elif j == 2:
    print(time[-4:])
elif j == 3:
   for c in sorted(time):
       print(c)
elif j == 4:
    for c in sorted(time):
        print(c)
    t = ''
    while t not in time:
        t = str(input('Qual time quer a posição: ')).strip()
    print(f'A posição do {t} está em {time.index(t)}º lugar')
print('Obrigado e volte sempre.')

########################################################################################################################

# GUANABARA

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
