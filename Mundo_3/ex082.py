"""
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
par = []
impar = []
valores = []
while True:
    op = (int(input('Digite um valor: ')))
    valores.append(op)
    resp = str(input("Quer continuar: [S/N]"))
    if op % 2 == 0:
        par.append(op)
        par.sort()
    else:
        impar.append(op)
        impar.sort()
    if resp in 'Nn':
        break
print(f'A lista completa foi: {valores}')
print(f'A lista de Pares é: {par}')
print(f'A lista de Ímpares é: {impar}')
