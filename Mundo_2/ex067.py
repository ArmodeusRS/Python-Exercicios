"""
Exercício Python 67: Faça um programa que mostre a tabuada
de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

num0 = int(input('Digite o número para ver sua tabuada: '))
cont = 1

while num0 >= 0:
    while cont < 11:
        mult = num0 * cont
        print(f'{num0} X {cont} = {mult}')
        cont += 1

    num0 = int(input('Digite o número para ver sua tabuada: '))
    cont = 1



