import math
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hipo = math.hypot(n1, n2)
print(f'A hipotenusa de {n1} e {n2} é {hipo:.2f}')

