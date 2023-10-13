km = float(input('Quantos quilômetros?: '))
d = int(input('Quantos dias de aluguel?: '))
valor = (d * 60) + (km * 0.15)
print('O valor total é de R$ {:.2f}'.format(valor))