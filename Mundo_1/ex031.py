n1 = int(input('Qual a distância em KM da viagem do Ônibus?'))

if n1 <= 200:
    n2 = float(n1 * 0.50)
    print(f'Sua viagem é de {n1} Km, o valor da sua passagem é de R${n2:.2f}')
else:
    n2 = float(n1 * 0.45)
    print(f'Sua viagem é de {n1} Km, o valor da sua passagem é de R${n2:.2f}')
