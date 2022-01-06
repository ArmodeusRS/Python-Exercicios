n1 = str(input('Digite um número: '))

if len(n1) == 4:
    print('Unidade:', n1[3])
    print('Dezena :', n1[2])
    print('Centena:', n1[1])
    print('Milhar :', n1[0])
elif len(n1) == 3:
    print('Unidade:', n1[2])
    print('Dezena :', n1[1])
    print('Centena:', n1[0])
elif len(n1) == 2:
    print('Unidade:', n1[1])
    print('Dezena :', n1[0])
elif len(n1) == 1:
    print('Unidade', n1[0])

#Solução Guanabara

num = int(input("Informe um número"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Unidade: {}'.format(d))
print('Unidade: {}'.format(c))
print('Unidade: {}'.format(m))
