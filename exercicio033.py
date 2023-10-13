n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

m = n1

if n2 > m:
    m = n2
if n3 > m:
    m = n3
print(f'O maior número é {m}.')

mn = n1

if n2 < mn:
    mn = n2
if n3 < mn:
    mn = n3
print(f'O menor número é {mn}.')