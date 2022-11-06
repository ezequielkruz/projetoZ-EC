print('\033[33;1m██████████ AULA 18 ██████████')

print('\033[34;1mNessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. '
      '\nAs listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, '
      '\nacessíveis por chaves individuais.')

print()
########################################################################################################################
dados = list()
dados.append('Pedro')
dados.append(25)
########################################################################################################################
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
########################################################################################################################
print(dados[0])
########################################################################################################################
print(dados[1])
print(dados)
########################################################################################################################
pessoas = list()
pessoas.append(dados[:]) # isso aqui gera uma copia na lista pessoas.
print(pessoas)
pessoas.remove(dados)
########################################################################################################################
print(pessoas)
pessoas.append(dados[0:2])
print(pessoas)
########################################################################################################################
pessoas.append(dados[2:4])
print(pessoas)
########################################################################################################################
pessoas.append(dados[4:6])
print(pessoas)
########################################################################################################################
print(pessoas[0][0]) # lista dentro de outra lista
print(pessoas)
########################################################################################################################
print(pessoas[1][1])
print(pessoas)
########################################################################################################################
print(pessoas[2][0])
print(pessoas)
########################################################################################################################
print(pessoas[1])
print(pessoas)
########################################################################################################################
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
########################################################################################################################
galera = list()
galera.append(teste[:]) # se caso não tenha [:], isso faz uma copia da lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) # [:] faz uma copia
print(galera)
galera.clear()
########################################################################################################################
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # uma lista dentro de outra lista. [[]]
print(galera)
########################################################################################################################
print(galera[0])
print(galera)
########################################################################################################################
print(galera[0][0])
print(galera)
########################################################################################################################
print(galera[2][1])
print(galera)
########################################################################################################################
for p in galera:
      print(p)
      print(p[0])
      print(p[1])
      print(f'{p[0]} tem {p[1]} anos de idade.')
galera.clear()
galera = list()
dado = list()
for c in range(0, 2):
      dado.append(str(input('Nome: ')))
      dado.append(int(input('Idade: ')))
      galera.append(dado[:]) # [:] esses 3 simbolos fazem a diferença.
      dado.clear()
print(dado)
print(galera)
########################################################################################################################
totmai = totmen = 0
for p in galera:
      if p[1] >= 21:
            print(f'{p[0]} é maior de idade.')
            totmai += 1
      else:
            print(f'{p[0]} é menor de idade.')
            totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')


