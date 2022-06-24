print('\033[34;1m{:█^80}'.format('.→ DESAFIO 86  ←.'))
print('\033[31;1mnome, peso, pessoas')
print('\033[33;1m--'*30)
#print('\033[38;1m')
########################################################################################################################
print('MATRIZ')

matriz = [[], [], []]
#matriz = []
for c in range(0, 9):
    if c <= 2:
        n = int(input(f'Digite um valor para [0, {c}]: '))
        matriz[0].append(n)
    elif c <= 5:
        n = int(input(f'Digite um valor para [1, {c-3}]: '))
        matriz[1].append(n)
    elif c <= 8:
        n = int(input(f'Digite um valor para [2, {c-6}]: '))
        matriz[2].append(n)
print(matriz)
print('\033[31;1m--'*30)
print('\033[32;1m{:=^60}'.format('MATRIZ'))
# 8 LINHAS #############################################################################################################
for c in matriz[0]:
    print(f'[ {c:^5} ]', end='')
print()
for c in matriz[1]:
    print(f'[ {c:^5} ]', end='')
print()
for c in matriz[2]:
    print(f'[ {c:^5} ]', end='')
print()
print('\033[32;1m='*60)
# 8 LINHAS #############################################################################################################
v = 0
for c in matriz: # se fosse uma matriz de 4 essa função seria mehor.
        for n in c:
            print(f'[ {n:^5} ]', end='')
            v += 1
            if v == 3:
                print()
                v = 0


