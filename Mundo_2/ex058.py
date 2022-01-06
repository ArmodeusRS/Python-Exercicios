"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador
vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint
from time import sleep

palpite = 1
computerChoice = randint(0, 10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar?')
userChoice = int(input('Qual o número que eu escolhi entre 0 e 10? '))
while userChoice != computerChoice:
    sleep(1)
    print('Não foi esse número.')
    if userChoice > computerChoice:
        palpite += 1
        sleep(0.5)
        print("Um pouco menos...")
        userChoice = int(input('Qual o número que eu escolhi entre 0 e 10? '))
    elif userChoice < computerChoice:
        palpite += 1
        sleep(0.5)
        print("Um pouco mais...")
        userChoice = int(input('Qual o número que eu escolhi entre 0 e 10? '))
if palpite == 1:
    print('Parabéns, acertou de primeira!!!!')
print(f'Você acertou em {palpite} tentativas!')
