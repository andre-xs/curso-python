from random import randint
from time import sleep

n = int(input('Digite um número de 0 a 5: '))
print('Processando...')
sleep(3)
num = (randint(1, 5))
print('O numero pensado pela máquina foi: {}.'.format(num))

if n == num:
    print('VOCÊ ACERTOU!')
else:
    print('Tente novamente.')