frase = 'Curso em Video Python'
print (frase[3])
print (frase[3:12])
print (frase[0:14:2])
print (frase[::5])
print (frase[::2])

print(frase.count('o'))
print(frase.upper().count('o'))

print(len(frase))
#print(len(frase.replace('Python', 'Android')))'''vai trocar apenas nessa instância'''
#frase = frase.replace('Python', 'Android') - para realmente fazer a troca de caracteres no programa

print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('video'))
print(frase.find('Video'))

print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])

#para imprimir um texto inteiro, da forma como está as linhas, colocamos 3 aspas

print ("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
It's also easy for beginners to use and learn, so jump in!""")