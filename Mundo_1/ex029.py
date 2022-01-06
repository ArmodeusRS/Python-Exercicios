print('='*25)
print('Controlador de Velocidade')
print('='*25)
n1 = int(input('Qual a velocidade do carro? '))
if n1 > 80:
    n2 = n1 - 80
    multa = (n1 - 80) * 7
    print('Você passou acima do limite de velocidade que é 80Km!')
    print(f'Voce passou a {n1}Km, {n2}Km acima do limite de velocidade.')
    print(f'O valor de sua multa é de R${multa:.2f}')
else:
    print('Boa Viagem!')
