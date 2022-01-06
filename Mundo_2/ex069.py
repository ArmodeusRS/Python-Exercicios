"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
homensCadastrados = 0  # B) quantos homens foram cadastrados.
maiorIdadeDezoito = 0  # A) quantas pessoas tem mais de 18 anos.
mulherMenorQueVinte = 0  # C) quantas mulheres tem menos de 20 anos.
cadastros = 0
homens = 0
mulheres = 0
op = 'S'
while True:

    if op == 'S':
        cadastros += 1
        print('=' * 30)
        print('CADASTRE UMA PESSOA')
        print('=' * 30)
        idade = int(input('Idade: '))
        sexo = str(input('[M/F] ')).strip().upper()[0]
        if idade >= 18:
            maiorIdadeDezoito += 1
        if sexo == 'F':
            mulheres += 1
            if idade < 20:
                mulherMenorQueVinte += 1
        if sexo == 'M':
            homens += 1
            homensCadastrados += 1
    elif op == 'N':
        break
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'Foram feitos {cadastros} cadastros.')
print(f'{homens} homens.')
print(f'{mulheres} mulheres.')
print(f'Das pessoas cadastradas {maiorIdadeDezoito} são maiores de 18 anos.')
print(f'Foram cadastrados {homensCadastrados} homens.')
print(f'{mulherMenorQueVinte} mulheres menores de 20 anos.')
