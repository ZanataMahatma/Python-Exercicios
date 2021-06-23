sexo = '0'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]:')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite novamente')

print('Acabou')