vel = float(input('Qual a velocidade do carro?: '))
print(f'A velocidade do carro é {vel}KM por hora.')

if vel > 80:
    d = vel - 80
    m = d * 7.00
    print('Sua velocidade está {}KM acima do limite permitido!'.format(d))
    print('Sua multa será de R${:.2f}.'.format(m))
else:
    print('Você está dentro do limite de velocidade.')