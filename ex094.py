ficha = dict()
listageral = list()
media = 0
cont = 0
while True:
    cont = cont + 1
    ficha['Nome'] = str(input('Nome: '))
    ficha['sexo'] = str(input('Sexo: [M/F] '))
    ficha['Idade'] = int(input('Idade: '))
    listageral.append(ficha.copy())
    resp = str(input('Deseja Continuar [S/N]'))
    if resp in 'Nn':
        break
print(listageral)
print(f'O grupo tem {cont} pessoas')
#print(f'A média de idade é de {media} anos.')
for i,v in enumerate(listageral):
    print(f'{sum(v["Idade"])}')