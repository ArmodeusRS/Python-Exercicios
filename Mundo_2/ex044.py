"""
Exercício Python 44: Elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""

n1 = float(input('Qual o preço do produto: R$ '))

avista = (n1 / 100) * 10
cvista = (n1 / 100) * 5
parcDuas = n1 / 2
parcTres = (n1 / 100) * 30
ttparcTres = n1 + parcTres
ttparcTresparc = ttparcTres / 3

op = int(input('Qual a forma de pagamento: \n1- Dinheiro ou Cheque à vista'
               '\n2- Cartão à vista\n3- Cartão 2x\n4- Cartão 3x\nDigite a opção desejada: '))

if op == 1:
    print('Você escolheu a opção 1: Dinheiro ou Cheque à vista.')
    print(f'Preço do produto R$ {n1:.2f} com desconto de 10% preço final R$ {n1 - avista:.2f}')
elif op == 2:
    print('Você escolheu a opção 2: Cartão à vista.')
    print(f'Preço do produto R$ {n1:.2f} com desconto de 5% preço final R$ {n1 - cvista:.2f}')
elif op == 3:
    print('Você escolheu a opção 3: Cartão 2x.')
    print(f'Preço do produto R$ {n1:.2f} sem desconto em 2x {parcDuas:.2f}')
elif op == 4:
    print('Você escolheu a opção 4: Cartão 3x ou mais.')
    print('Nesta opção juros de 20%!')
    print(f'Preço do produto R$ {n1:.2f} com juros de 20% preço final R$ {ttparcTres:.2f} em 3x {ttparcTresparc:.2f}')



