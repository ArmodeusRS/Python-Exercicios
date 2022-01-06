"""
Exercício 101:
Crie um programa que tenha uma função chamada voto() que
vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL ou OBRIGATÓRIO  nas eleições.
"""


def voto(num=0):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - num
    return idade


#    PROGRAMA PRINCIPAL
ano = int(input('Em que ano você nasceu? '))
svoto = voto(ano)
if 18 < svoto < 65:
    print(f'Com {svoto} anos: VOTO OBRIGATÓRIO.(Maior de 18 anos).')

elif 16 <= svoto < 18:
    print(f'Com {svoto} anos: VOTO OPCIONAL.(Entre 16 menor de 18 anos.).')
elif svoto >= 65:
    print(f'Com {svoto} anos: VOTO OPCIONAL.(Maiores de 65 anos.).')

else:
    print(f'Com {svoto} anos: VOTO NEGADO (Menor de 16 anos.).')
