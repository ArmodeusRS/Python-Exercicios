"""
Exercício Python 64: Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre
quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
num1 = 0
digitados = 0
while True:
    num = int(input('Digite um número, (Para sair 999): '))
    if num == 999:
        break
    digitados += 1
    num1 = num + num1
print(f'Você digitou {digitados} valores e a soma entre eles foi {num1}')

