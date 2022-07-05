print('\033[1;31mCrie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.\033[m')

print('\033[34m===== Desafio 06 =====\033[m')

n = int(input('Digite um número: '))
ndm = n * 2
ndp = n ** 2
ntm = n * 3
ntp = n ** 3
nrq = n ** (1/2)
nrc = n ** (1/3)
print('O dobro em multiplicação é: {}\n O dobro em potência é: {}\n O triplo em multiplicação é: {}\n O triplo em potência é: {}\n A raiz Quadrada é: {}\n A raiz Cúbica: {}'.format(ndm, ndp, ntm, ntp, nrq, nrc))

# Guanabara

n = int(input('Digite um númer0: '))
d = n * 2 # Se caso usar a variavel, guarda na memoria para usar a frente.
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))

# Atalho

n = int(input('Digite um número: '))
print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, (n**(1/2))))#pow(n, (1/2) calcula raiz quadrada

