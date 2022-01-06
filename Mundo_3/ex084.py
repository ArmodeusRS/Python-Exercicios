"""
Exercício Python 084:
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = list()
cadastros = 0
dado = []
maior = 0
menor = 100

while True:
    pes = str(input('Nome: '))
    dado.append(pes)
    peso = int(input('Peso: '))
    dado.append(peso)
    pessoas.append(dado[:])

    if peso > maior:
        maior = peso
        peso1 = [pes, peso]
    elif peso < menor:
        peso2 = [pes, peso]
        menor = peso
    dado.clear()
    cadastros += 1
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'S':
        pass
    else:
        break

print(pessoas)
print(f'Ao todo, você cadastrou {cadastros} pessoas.')
print(f'O maior peso foi de {peso1[0]}. Peso de {peso1[1]} kg.')
print(f'O menor peso foi de {peso2[0]}. Peso de {peso2[1]} Kg.')
