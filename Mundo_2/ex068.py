"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('Use números de 1 à 10.')
print('=-' * 20)
computerGame = randint(0, 10)
userGame = int(input('Digite sua jogada: '))


jogadaSoma = computerGame + userGame

contador = 1
ganhou = 0
while True:

    while userGame > 10:  # Validando até 10.
        print('Somente números inteiros até 10!')
        userGame = int(input('Digite sua jogada: '))

    parOuImparHuman = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 40)

    while True:  # Validando P ou I.
        if parOuImparHuman in 'PI':
            break
        else:
            print('Opção inválida, [P] para Par ou [I] para ímpar.')
            parOuImparHuman = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    if jogadaSoma % 2 == 0:
        if parOuImparHuman == 'I':
            print(f'Deu {jogadaSoma} Número Par! Você escolheu ímpar. Você perdeu!!')
            print(f'Você jogou {contador} vazes e ganhou {ganhou} vezes!')
            print('FIM DO JOGO! Obrigado por jogar!')
            break
        elif parOuImparHuman == 'P':
            print('=-' * 20)
            print(f'Deu {jogadaSoma} Número Par! Parabéns! Você GANHOU!')
            print('=-' * 20)
            ganhou += 1
    userGame = int(input('Digite sua jogada: '))


print('Fim!')
