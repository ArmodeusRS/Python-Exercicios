import random
n2 = []
n1 = ''

for c in range(4):
    n1 = str(input(f'Digite o nome do aluno {c +1}: '))
    n3 = n2.append(n1)

sortear = random.choice(n2)
print(f'O aluno escolhido foi {sortear}.')
