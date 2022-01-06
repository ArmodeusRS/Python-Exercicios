"""
Exercício Python 37: Escreva um programa em Python que
leia um número inteiro qualquer e peça para o usuário escolher qual
será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

n1 = int(input('Digite um número: '))
print('Qual será a base de conversão? \n-1 para Binário.\n-2 para Octal.\n-3 para Hexadecimal.')
n2 = int(input('Digite a opção escolhida: '))

if n2 == 1:
    print(f'{n1} em Binário:')
    print(bin(n1)[2:])
elif n2 == 2:
    print(f'{n1} em Octal:')
    print(oct(n1)[2:])
elif n2 == 3:
    print(f'{n1} em Hexadecimal:')
    print(hex(n1)[2:])
