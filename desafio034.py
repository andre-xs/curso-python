s = float(input('Qual o seu salário?: '))

if s <= 1250:
    a = s + (s * 0.1)
    t = s + a
    print('Você vai receber um aumento de R$ {}. Seu salário atualizado será de R$ {}.'.format(a, t))
else:
    a = s * 0.15
    t = s + a
    print('Você vai receber um aumento de R$ {}. Seu salário atualizado será de R$ {}.'.format(a, t))
