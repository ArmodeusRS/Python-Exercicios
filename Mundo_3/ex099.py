"""
Exercício 099:
Faça um programa que tenha uma função chamada maior(), que receba
vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

"""


def maior(*num):
    from time import sleep
    lista = []
    lista = num
    elementos = len(lista)
    print('-=' * 30)
    print('Analisando os valores passados...')
    num = 0
    for v in lista:
        print(f'{v}', end=' ')
        sleep(0.5)
        if v > num:
            num = v
    print(f'Foram informados {elementos} valores ao todo.')
    print(f'O maior valor informado foi {num}.')


maior(1, 2, 2, 5, 7)
maior(2, 3, 4)
maior(15, 12, 1, 3, 5, 4)
maior(6)
