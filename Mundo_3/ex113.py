"""
Exercício Python 113:
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leint(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('ERRO! Por valor digite apenas números inteiros!')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return

        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('ERRO! Por valor digite apenas número Real!')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return

        else:
            return n


# PROGRAMA PRINCIPAL

n1 = leint('Digite um Inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor Inteiro digitado foi {n1} o Real foi {n2}')
