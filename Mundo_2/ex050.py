"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
lista = []
for c in range(6):
    n0 = int(input('Digite um número: '))
    if n0 % 2 == 0:
        lista.append(n0)


n1 = sum(lista)
print(f'O total da soma dos números pares é {n1}')

