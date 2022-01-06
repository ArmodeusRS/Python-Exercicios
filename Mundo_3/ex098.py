"""
Exercício 098:
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo.
e realize a contagem.
Seu programa tem que realizar três contagens através da função.
a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalizada.
"""


def contador():
    from time import sleep
    c = 1
    print('-=' * 20)
    print('Contagem de 1 até 10 contando de 1 em 1.')
    print('-=' * 20)
    for c in range(1, 11):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('Fim!')

    print('-=' * 20)
    print('Contagem de 10 até 0 contando de 2 em 2.')
    print('-=' * 20)
    c = 12
    while c > 0:
        c -= 2
        print(f'{c}', end=' ')
        sleep(0.5)
    print('Fim!')
    print('-=' * 20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = abs(passo)
    if inicio < fim:
        print('-=' * 20)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        print(f'{inicio}', end=' ')

        while inicio <= fim:
            inicio = inicio + passo
            print(f'{inicio}', end=' ')
            if inicio + passo > fim:
                break
        print('Fim!')
    if inicio > fim:
        print('-=' * 20)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        print(f'{inicio}', end=' ')

        while inicio >= fim:
            inicio = inicio - passo
            print(f'{inicio}', end=' ')
            if inicio - passo < fim:
                break
        print('Fim!')
        print()


contador()
