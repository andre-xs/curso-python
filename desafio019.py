import random

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')

sorteado = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno sorteado foi o aluno: {}'.format(sorteado))