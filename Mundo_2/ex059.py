"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

sairDoPrograma = False
var1 = 0
var2 = 0
op = 0
for c in range(2):
    valor = int(input('Digite um valor: '))
    if c == 0:
        var1 = valor
    else:
        var2 = valor
while not sairDoPrograma:
    print('')
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    ''')
    op = int(input('Digite sua opção: '))
    if op == 1:  # Somar
        resp = var1 + var2
        print(f'A soma entre {var1} e {var2} é {resp} !!')
    elif op == 2:  # Multiplica
        resp = var1 * var2
        print(f'A muçtiplicação entre {var1} e {var2} é {resp} !!')
        print('')

    elif op == 3:  # Maior
        if var1 > var2:
            print(f'O maior entre {var1} e {var2} é {var1}!!')
            print('')
        else:
            print(f'O maior entre {var1} e {var2} é {var2}!!')
            print('')

    elif op == 4:  # Novos Valores
        print('Digite novos valores.')
        for c in range(2):
            valor = int(input('Digite um valor: '))
            if c == 0:
                var1 = valor
            else:
                var2 = valor
    elif op == 5:
        sairDoPrograma = True
    else:
        print('Opção inválida. Tente novamente!')






