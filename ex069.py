idade = sexo = cont18 = homem = mulher = 0
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
print(f'E temos {mulher} mulher com menos de 20 anos')