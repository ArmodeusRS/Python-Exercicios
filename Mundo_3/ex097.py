"""
Exercício 097:
Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def escreva(msg):
    tamanho = len(msg) + 2
    print('~' * tamanho)
    print('', msg, '')
    print('~' * tamanho)


escreva('camarada')

escreva('Insconstitucionalicimamente')

escreva('Alambrado Celebrando')

escreva('CeV')

escreva('Olá, Mundo!')

