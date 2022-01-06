n1 = str(input('Digite seu nome: '))
n2 = n1.upper()
n2.find('SILVA')
if n2.find('SILVA') == -1:
    print('Não existe Silva no seu nome!')

else:
    print('Existe Silva no seu nome!')


#Solução Guanabara

nome = str(input('Qual o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
