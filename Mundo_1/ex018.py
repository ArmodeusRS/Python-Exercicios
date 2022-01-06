import math
n1 = float(input('Digite o ângulo que você deseja: '))
n2 = math.sin(math.radians(n1))
n3 = math.cos(math.radians(n1))
n4 = math.tan(math.radians(n1))

print(f'O ângulo de {n1} tem o SENO de {n2:.2F}')
print(f'O ângulo de {n1} tem o COSSENO de {n3:.2F}')
print(f'O ângulo de {n1} tem o TANGENTE de {n4:.2F}')
#print(f'Dado o valor {n1}, seu Seno é {n2}, Cosseno {n3} e Tangente é {n4}')
# Tem que conver ter o número coletado primeiro pra Radiando, para o python considerar como Graus.
