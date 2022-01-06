"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
from time import sleep

casa = float(input('Qual o valor do imóvel? R$ '))
renda = float(input('Qual o valor total de sua renda? R$ '))
tempo = float(input('Em quantos anos seria o financiamento? '))

prest_limit = (renda / 100) * 30
tempo_mes = int(tempo * 12)
prest_ano = casa / tempo_mes

print(f'O valor da casa é de R$ {casa:.2f} dividido por {tempo_mes} meses.')
print(f'O valor máximo de sua prestação não pode exceder R$ {prest_limit:.2f}')
sleep(1)
print('Analisando...')
sleep(2)

if prest_ano <= prest_limit:
    print(f'Sua prestação ficou no valor mensal de {prest_ano:.2f} e está dentro do limite de 30% de sua renda.')
    print('Seu financiamento foi aprovado! Parabéns!')
elif prest_ano> prest_limit:
    print(f'Sua prestação ficou no valor mensal de {prest_ano:.2f} e '
          f'\nestá acima do limite de 30% de sua renda R$ {prest_limit:.2f}.')
    print('Seu financiamento foi negado!')
