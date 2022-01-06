"""
Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
print('                      BRASILEIRÃO 2020')
print('-=-' * 20)
times = ('Flamengo', 'Interncaional', 'Atlético MG', 'São Paulo', 'Fluminense', 'Grêmio',
         'Palmeiras', 'Santos', 'Athletico', 'Bragantino', 'Ceará', 'Corinthians',
         'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print('Os cinco primeiros colocados foram: ', times[:5])
print('-=-' * 20)
print('Os quatro últimos colocados foram: ', times[-4:])
print('-=-' * 20)
timesOrder = sorted(times)
print('Times em Ordem Alfabética:')

print(timesOrder)
print('-=-' * 20)
print('O Bragantino está na ', times.index('Bragantino'), 'ª posição!')

