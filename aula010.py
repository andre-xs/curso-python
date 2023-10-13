'''Condições

CONDIÇÃO SIMPLES

nome = str(input('Qual é o seu nome?: '))
if nome == 'André':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))


CONDIÇÃO COMPOSTA
tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('--Fim--')