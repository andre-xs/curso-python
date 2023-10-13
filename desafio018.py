import math

ang = float(input('Ângulo: '))
rad = math.radians(ang)
print('O seno desse ângulo é {:.2f}, o cosseno desse ângulo é {:.2f} e a tangente é {:.2f}.'.format(math.sin(rad), math.cos(rad),math.tan(rad)))