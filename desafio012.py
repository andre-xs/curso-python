preco = float(input('Qual o preço do produto?: '))
desc = preco * 0.05
final = preco - desc

print('Esse produto vai receber R$ {:.2f} de desconto.'.format(desc))
print('O valor final será de R$ {:.2f}.'.format(final))