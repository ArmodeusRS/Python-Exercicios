"""
Exercício Python 106:
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
"""
c = ('\033[m',         # 0  sem cores
     '\033[0;30;41m',  # 1  Veremelho
     '\033[0;30;42m',  # 2  Verde
     '\033[0;30;43m',  # 3  Amarelo
     '\033[0;30;44m',  # 4  Azul
     '\033[0;30;45m',  # 5  Roxo
     '\033[0;30m',     # 6  Branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando\'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[6], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Bibliotéca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
