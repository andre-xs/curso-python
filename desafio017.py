from math import hypot
ca1 = float(input('Digite o cateto oposto:'))
ca2 = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(ca1, ca2)
print(f'Os catetos são {ca1} e {ca2} e a hipotenusa é {hipotenusa}.')