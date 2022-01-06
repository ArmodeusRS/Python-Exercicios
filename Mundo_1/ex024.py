n1 = str(input('Em que cidade você nasceu? '))
n2 = n1.upper()
n2.find('SANTO')
if n2.find('SANTO') == -1:
    print('Não existe Santo no nome de sua cidade!')

elif n2.find("SANTO") == 0:
    print('O nome de sua cidade começa com Santo!')
else:
    print('Seu nome tem Santo, mas não inicia o seu nome!')

# Solução Guanabara

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
