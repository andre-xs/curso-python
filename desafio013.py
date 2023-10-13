sal = float(input('Qual o seu salário?: '))
a = sal * 0.15
final = sal + a

print('Você vai receber um aumento de R$ {:.2f} no seu salário.'.format(a))
print('Seu salário total será de R$ {:.2f}.'.format(final))