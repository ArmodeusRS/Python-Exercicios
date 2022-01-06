"""
Exercício Python 071: Crie um programa que simule o funcionamento de
um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('\033[30m-=:=-\033[m'*5)
print('\033[30m{:^25}\033[m'.format('Banco'))
print('\033[30m-=:=-\033[m'*5)
while True:
    saque = int(input('Valor p/ saque: R$'))
    cinquenta = saque // 50
    vinte = (saque - 50 * cinquenta) // 20
    dez = ((saque - 50 * cinquenta) - 20 * vinte) // 10
    um = (((saque - 50 * cinquenta) - 20 * vinte) - 10 * dez) // 1
    print('\033[30m-=:=-\033[m' * 5)
    print(f'Sacando:\n->{cinquenta} cédulas de R$50\n->{vinte} cédulas de R$20')
    print(f'->{dez} cédulas de R$10\n->{um} cédulas de R$1')
    print('\033[30m-=:=-\033[m' * 5)
    continuar = input('Continuar a sacar?[S/N] ').strip().upper()[0]
    print('\033[30m-=:=-\033[m' * 5)
    while continuar not in 'SN':
        continuar = input('Continuar a sacar?[S/N] ').strip().upper()[0]
    if continuar == 'N':
        break