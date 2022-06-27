print('21. “Há apenas uma maneira de evitar críticas: não fazer, não falar e não ser nada.” – Aristóteles')

# 'Curso em Video Python' = Cadeia de caracteres = string

print('P1')
frase = 'Curso em Video Python'
print(frase[::2])

print('P2')
print(frase[3])

print('P3')
print(frase[3:13])

print('P4')
print(frase[:13])
print(frase[1:15:2])
print(frase[:13:2])


print('P5')
print('''Nessa aula, vamos aprender operações com String no 
Python. As principais operações que vamos aprender
são o Fatiamento de String, Análise com len(), 
count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), 
junção com join().''')

print('P6')
print(frase.count('o'))

print('P7')
print(frase.upper().count('O'))

print('P8')
print(len(frase)) # len conta quantos caracteres tem uma string, espaço tambem conta.

print('P9')
frase = '   Curso em Video Python'
print(len(frase.strip())) # strip tira os espaços na string

print('P9')
frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android')) # replace tem a possibilidade de muda as letras da string

print('P10')
print('''frase[0] = 'J' # A string em micro espaço é imutavel. tem que usar um metodo.''')
#frase[0] = 'J' # A string em micro espaços é imutavel. tem que usar um metodo.

print('P11')
frase.replace('Python', 'Android') # Aqui o replace não foi salvo, então não aparece no print nessa estancia.
print(frase)

print('P12')
frase = frase.replace('Python', 'Android') # Aqui utiliza uma função de transfomação de string e faça uma atribuição. agora esta salva.
print(frase)

print('P13')
frase = 'Curso em Video Python'
print('Python' in frase) # Existe a palavra na variavel
print(frase)
frase = frase.replace('Python', 'Android') # Aqui esta salva a variavel.
print(frase)
print('Python' in frase) # True ou False se tem a palavra na string

print('P14')
print(frase.find('Curso')) # Posição zero

print('P15')
print(frase.find('Video')) # Posição nove

print('P16')
print(frase.find('video')) # Posição nao encontrada -1.

print('P17')
print(frase.lower().find('video')) # Posição nove, nesse caso encontro por causa da função lower

print('P18')
print(frase.split()) # transforma a string em uma lista de palavras.

print('P19')
dividido = frase.split() # atribui a variavel a outra varivel mas como em forma de lista.
print(dividido[0])

print('P20')
print(dividido[0], dividido[1]) # A a variavel dividido escolha uma palavra da lista.






