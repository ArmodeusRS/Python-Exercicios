from random import randint

sorteia = randint(0, 5)

n1 = int(input('Qual número entre 0 e 5 eu escolhi? '))
if n1 == sorteia:
    print(f'Você acertou ! eu escolhi {sorteia}, você venceu!')
else:
    print(f'Você errou! eu escolhi {sorteia}')

# Solução Guanabara

