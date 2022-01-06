"""
Exercício 096:
Faça um programa que tenha uma função chamada area()
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a area do terreno.
"""


def area():
    print()
    print('Controle de Terrenos')
    print('--------------------')
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO: (m): '))
    areaa = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {areaa}m².')


area()


# Resolução Guanabara

def area1(larg, comp):
    areaa = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {areaa}m².')


# PROGRAMA PRINCIPAL


print('--------------------')
print('Controle de Terrenos')
print('--------------------')

laa = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO: (m): '))
area1(laa, com)

