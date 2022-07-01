print('\033[1;31m', '-=-'*20)
print('-=-=-=- AULA 11 -=-=-=-')
print('-=-\033[m'*20)

# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python.
# Veja como utilizar o código \033[m com todas as suas principais possibilidades.

#   ANSI escape sequence

#   \033[m
#   \033[style=fonte; text = cor; back=fundo m
#   \033[0;33;44m

#   STYLE = Tipo de Fonte
#   0 none
#   1 Bold = Negrito
#   4 Underline
#   7 Negative

#   TEXT = Cor do texto
#   30 BRANCO = PRETO
#   31 VERMELHO
#   32 VERDE
#   33 AMARELO
#   34 AZUL
#   35 ROXO
#   36 CELESTE
#   37 CINZA
#   38 BRANCO

#   BACK = Fundo do texto
#   40 BRANCO
#   41 VERMLHO
#   42 VERDE
#   43 AMARELO
#   44 AZUL
#   45 ROXO
#   46 CELESTE
#   47 CINZA

print('\033[0;30;41m    Teste')
print('\033[4;33;44m    Teste')
print('\033[1;35;43m    Teste')
print('\033[30;42m      Teste')
print('\033[m           Teste')
print('\033[7;30m       Teste')

print('\033[31mOla, mundo!')
print('\033[31;43mOla, mundo!')
print('\033[1;31;43mOla, mundo!\033[m')
print('\033[4;30;45mOla, mundo!\033[m')
print('\033[30mOla, mundo!\033[m')
print('\033[7;30mOla, mundo!\033[m')
print('\033[0;33;44mOla, mundo!\033[m')
print('\033[7;33;44mOla, mundo!\033[m')


print('\033[38m-=-\033[m'*20) # Abaixo são as cores, somente usar em texto dentro ''

print('\033[30mOla, mundo!\033[m') #    PRETO
print('\033[31mOla, mundo!\033[m') #    VERMELHO
print('\033[32mOla, mundo!\033[m') #    VERDE
print('\033[33mOla, mundo!\033[m') #    AMARELO
print('\033[34mOla, mundo!\033[m') #    AZUL
print('\033[35mOla, mundo!\033[m') #    ROXO
print('\033[36mOla, mundo!\033[m') #    CELESTE
print('\033[37mOla, mundo!\033[m') #    CINZA
print('\033[38mOla, mundo!\033[m') #    BRANCO

print('\033[34m-=-\033[m'*20) # Abaixo sao os fundos

print('\033[30;40mOla, mundo!\033[m') # PRETO
print('\033[31;41mOla, mundo!\033[m')
print('\033[32;42mOla, mundo!\033[m')
print('\033[33;43mOla, mundo!\033[m')
print('\033[34;44mOla, mundo!\033[m')
print('\033[35;45mOla, mundo!\033[m')
print('\033[36;46mOla, mundo!\033[m')
print('\033[37;47mOla, mundo!\033[m')
print('\033[38;48mOla, mundo!\033[m') # Fundo normal

print('\033[34m-=-\033[m'*20)

a = 3
b = 5
print('Os valores são \033[32m {} \033[m e \033[31m {} \033[m !!!'.format(a, b))

print('\033[38m-=-\033[m'*20)

nome = 'Guanabara'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

print('\033[38m-=-\033[m'*20)

cores = {'limpa':'\033[m',  # Biblioteca
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
nome = 'Guanabara'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))




