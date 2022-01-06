"""
Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a
criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista1 = []
print('-=' * 30)
print('                    JOGA NA MEGA SENA')
print('-=' * 30)
jogavezes = int(input('Quantos jogos você quer que eu sorteie?>>> '))
print('')
print('-=' * 30)
print(f'Sorteando {jogavezes} jogos!')
print('-=' * 30)
sleep(1)
for c in range(jogavezes):

    for cont in range(0, 6):
        sortedado = randint(1, 60)
        if sortedado in lista1:
            pass
        else:
            lista1.append(sortedado)
    c += 1
    lista1.sort()
    print(f'Jogo {c}: ', lista1)
    lista1.clear()
print('-=' * 10, end='')
print('<BOA SORTE!>', end='')
print('-=' * 10)
