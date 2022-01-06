"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes


"""

print('='*25)
print('Analisador de Triângulos')
print('='*25)

r1 = float(input('Digite o primeiro segmento de reta:'))
r2 = float(input('Digite o segundo  segmento de reta:'))
r3 = float(input('Digite o terceiro segmento de reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM formar um TRIÂNGULO ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO PODEM formar um TRIÂNGULO!')
