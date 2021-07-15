'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
#correção
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 =+ 1
    if sexo == 'M':
        totH =+ 1
    if sexo == 'F' and idade < 20:
        totM20 =+ 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulher com menos de 20 anos')

# minha resposta
'''idade = sexo = cont18 = homem = mulher = 0
continuar = 'S'

while continuar == 'S':
    print('--' * 20)
    print('CADASTRE UMA PESSOA')
    print('--' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        cont18 = cont18 + 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade <= 20:
        mulher = mulher + 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]


print('=='*20)
print(f'Total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulher com menos de 20 anos')'''