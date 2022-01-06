"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada
de um número que o usuário escolher, só que agora utilizando um laço for.
"""
n0 = int(input('Digite o número para a tabuada: '))
for c in range(1, 11):
    n1 = n0 * c
    print(f'{n0} * {c} = {n1}')

