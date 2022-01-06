n1 = float(input('Digite a largura da parede: '))
n2 = float(input('Digite a altura  da parede: '))
n3 = int(input('Quantas demãos de tinta: '))
area = (n1 * n2) * n3
tinta = area / 2
print(f'A àrea total de pintura é de {area}m², com {n3} demão de tinta, será necessário {tinta} latas de tinta. ')

