"""
Exercício Python 72:
Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. Seu programa deverá ler
um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""


numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
op = int(input('Digite um número entre 0 e 10: '))

while True:
    if 0 <= op <= 10:
        break
    else:
        print('Opção inválida! Digite números entre 0 e 10!')
        op = int(input('Digite um número entre 0 e 10: '))

print(f'Você digitou o número {numeros[op]}!')
