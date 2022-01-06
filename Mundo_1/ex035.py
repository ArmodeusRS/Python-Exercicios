print('='*25)
print('Analisador de Triângulos')
print('='*25)

r1 = float(input('Digite o primeiro segmento de reta:'))
r2 = float(input('Digite o segundo  segmento de reta:'))
r3 = float(input('Digite o terceiro segmento de reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM formar um TRIÂNGULO!')
else:
    print('Os segmentos NÃO PODEM formar um TRIÂNGULO!')
