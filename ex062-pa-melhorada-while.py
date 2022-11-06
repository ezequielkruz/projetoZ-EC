print('\033[33;1m-='*30)
print('\033[34;1m→.→.→.→.→ DESAFIO 62 ←.←.←.←.←')
print('\033[33;1m-='*30)

print('\033[31;1mMelhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. '
      '\nO programa encerrará quando ele disser que quer mostrar 0 termos. ')

print('\033[33;1m-='*30)
print('\033[38;1m')

########################################################################################################################

print('()()()()() PROGRESSÃO ARITMETICA MENU ()()()()()')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = int(input('Qual termo da PA: '))
decimo = primeiro + (pa - 1) * razao
a = 0
p = 1
print(pa)
while a < decimo: # fazer um ciclo, ate o valor se igualar. usando (!=) ou (<)
    a = primeiro + razao # o (a) vai recebe o valor da soma
    primeiro = a # o (primeiro) vai retorna o valor para o ciclo
    p += 1 # aqui para a posição de cada ciclo, é opcional
    print('A posição {}ª, da PA é {}.'.format(p, a))
    if a == decimo: # quando o valor se igualar, chama esse opção para ver o que o usuario vai decidir.
        print('\033[34;1m')
        inf = int(input('Ver mais termos da PA?'
                        '\nDigite valor ou [0] para sair: '))
        if inf > 0: # se o usuario decide saber quantos PA poder ter ainda. usando (!=) ou (>)
            pa = inf + 1
            decimo = primeiro + (pa - 1) * razao
            print(pa)
        else:
            print('Obrigado pela preferencia.')

print('FIM')

########################################################################################################################

# GUANABARA
print('\033[34;1m')

print('Gerador de PA')
print(' -=' * 10 )
primeiro = int(input(' Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))



