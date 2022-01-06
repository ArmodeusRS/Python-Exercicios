"""
Exercício Python 39: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já
passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

n1 = int(input('Digite o ano de seu nascimento: '))

idade = 2021 - n1

if idade < 18:
    resta = 18 - idade
    print(f'Você está com {idade} anos e ainda faltam {resta} ano(s) para você se alistar!')
elif idade > 18:
    passou = idade - 18
    print(f'Você está com {idade} anos e passou {passou} anos(s) do período de alistamento!')
elif idade == 18:
    print(f'Você está com {idade} anos e deve fazer o seu alistamento militar!')
