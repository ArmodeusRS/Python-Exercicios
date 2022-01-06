"""
Exercício Python 085:
Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
par = []
impar = []
valores = []

for c in range(1, 8):
    op = (int(input(f'Digite o {c}° valor: ')))
    valores.append(op)

    if op % 2 == 0:
        par.append(op)
        par.sort()
    else:
        impar.append(op)
        impar.sort()


print(f'A lista de Pares é: {par}')
print(f'A lista de Ímpares é: {impar}')