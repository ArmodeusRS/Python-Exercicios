"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.


"""

from random import randint
from time import sleep

#JoKenPô

print('=' * 20)
print('       JOKENPÔ')
print('=' * 20)

print('Escolha: \n1- PEDRA \n2- PAPEL \n3- TESOURA')
n0 = int(input('Digite sua opção: '))

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(1)
computerChoice = randint(1, 3)
n1 = 'PEDRA'
n2 = 'PAPEL'
n3 = 'TESOURA'


# Condição Empate.
if n0 == 1 and computerChoice == 1:
    print(f'Você escolheu {n1} o computador escolheu {n1}')
    print('EMPATE!!')
elif n0 == 2 and computerChoice == 2:
    print(f'Você escolheu {n2} o computador escolheu {n2}')
    print('EMPATE!!')
elif n0 == 3 and computerChoice == 3:
    print(f'Você escolheu {n3} o computador escolheu {n3}')
    print('EMPATE!!')

# Vitória Jogador.
if n0 == 1 and computerChoice == 3:
    print(f'Você escolheu {n1} o computador escolheu {n3}')  # Vitória Pedra(1) x Tesoura(3)
    print('Parabéns você Venceu!!!!')

elif n0 == 2 and computerChoice == 1:
    print(f'Você escolheu {n2} o computador escolheu {n1}')  # Vitória Papel(2) x Pedra(1)
    print('Parabéns você Venceu!!!!')

elif n0 == 3 and computerChoice == 2:
    print(f'Você escolheu {n3} o computador escolheu {n2}')  # Vitória Tesoura(3) x Papel(2)
    print('Parabéns você Venceu!!!!')

# Vitória Computador.

elif computerChoice == 1 and n0 == 3:
    print(f'O Computador escolheu {n1} você escolheu {n3}')  # Vitória Pedra(1) x Tesoura(3)
    print('COMPUTADOR VENCEU!!!!')

elif computerChoice == 2 and n0 == 1:
    print(f'O Computador escolheu {n2} você escolheu {n1}')  # Vitória Papel(2) x Pedra(1)
    print('COMPUTADOR VENCEU!!!!')

elif computerChoice == 3 and n0 == 2:
    print(f'O Computador escolheu {n3} você escolheu {n2}')  # Vitória Tesoura(3) x Papel(2)
    print('COMPUTADOR VENCEU!!!!')
