"""
Exercício Python 041: A Confederação Nacional de Natação precisa de
um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

ano = int(input('Digite o ano do seu nascimento: '))

idade = 2021 - ano

if idade <= 9:
    print(f'Você tem {idade} anos e sua categoria é MIRIM!')
elif 14 >= idade > 9:
    print(f'Você tem {idade} anos e sua categoria é INFANTIL!')
elif 19 >= idade > 14:
    print(f'Você tem {idade} anos e sua categoria é JUNIOR!')
elif 21 >= idade > 20:
    print(f'Você tem {idade} anos e sua categoria é SÊNIOR!')
else:
    print(f'Você tem {idade} anos e sua categoria é MASTER!')
