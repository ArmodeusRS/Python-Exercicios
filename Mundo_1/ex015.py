n1 = float(input('O Carro rodou quantos KM: '))
n2 = int(input('Por quantos dias o carro foi alugado: '))
dias = n2 * 60
km = n1 * 0.15
total = km + dias

print(f'Por {n2} dias de aluguel R${dias:.2f}, por {n1}Km rodados R${km:.2f} gerando o valor total de R${total:.2f}')
