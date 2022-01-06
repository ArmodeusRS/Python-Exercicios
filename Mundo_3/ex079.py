"""
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários
valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""
lista = []
cont = 0
while True:
    cont = 2
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso...')
        lista.append(num)
    if cont > 1:
        op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if op == 'S':
            pass
        else:
            break
lista.sort()
print(f'Você digtou os valores:', lista)
