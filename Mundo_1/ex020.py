import random
n2 = []
n1 = ''

for c in range(4):
    n1 = str(input(f'Digite o nome do aluno {c+1}: '))
    n3 = n2.append(n1)

random.shuffle(n2)

print('A ordem de apresentação dos trabalhos é: ')
for c in range(4):
    print(n2[c])
