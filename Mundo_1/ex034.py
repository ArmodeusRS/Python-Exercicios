n1 = float(input('Digite o valor do salário: R$ '))

if n1 > 1250:
    n2 = (n1 / 100) * 10
    n3 = n1 + n2
    print(f'Seu salário é de R$ {n1:.2f}, com um aumento de 10% R$ {n2:.2f} ')
    print(f'tem seu valor final atualizado para R$ {n3:.2f}')
elif n1 <= 1250:
    n2 = (n1 / 100) * 15
    n3 = n1 + n2
    print(f'Seu salário é de R$ {n1:.2f}, com um aumento de 15% R$ {n2:.2f} ')
    print(f'tem seu valor final atualizado para R$ {n3:.2f}')
