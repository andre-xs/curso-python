d = float(input('Qual a distância da viagem?: '))

if d <= 200:
    v = d * 0.5
    print('Sua viagem vai custar R$ 0,50 por KM. Totalizando R$ {:.2f}.'.format(v))
else:
    v = d * 0.45
    print('Sua viagem vai custar R$ 0,45 por KM. Totalizando R$ {:.2f}.'.format(v))
