"""
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de
uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
"""

print('=' * 20)
print('      TABELA IMC')
print('=' * 20)
print('')
altura = float(input('Digite sua altura: (m) '))
peso = float(input('Digite seu peso: (Kg) '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} \nabaixo de 18.5: ABAIXO DO PESO NORMAL!')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é de {imc:.2f} \nentre 18.5 e 25: PESO IDEAL.!')
elif 25 < imc <= 30:
    print(f'Seu IMC é de {imc:.2f} \nentre 25 e 30: SOBREPESO!')
elif 30 < imc <= 40:
    print(f'Seu IMC é de {imc:.2f} \nentre 30 e 40: OBESIDADE!')
else:
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    print('Acima de 40: Obesidade Mórbida. SAÚDE EM RISCO!')
