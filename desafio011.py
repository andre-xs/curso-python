l = float(input('Qual a largura da parede?: '))
a = float(input('Qual a altura da parede?: '))

area = l * a
ltinta = area / 2

print('A área total que será pintada é de {}m².'.format(area))
print('Você precisará de {} litros de tinta para pintar toda essa área.'.format(ltinta))