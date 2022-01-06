# COLETA
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

# MAIOR
if n1 > n2 and n1 > n3:
    print(f'{n1} é o MAIOR!')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o MAIOR!')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é o MAIOR!')

# MENOR
if n1 < n2 and n1< n3:
    print(f'{n1} é o MENOR!')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o MENOR!')
elif n3 < n1 and n3 < n2:
    print(f'{n3} é o MENOR!')
