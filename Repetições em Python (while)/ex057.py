'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

# minha resposta
'''sexo = '0'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]:'))
    if sexo != 'M' and sexo != 'F':
        print('Digite novamente')

print('Acabou')'''
# correção

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Porfavor,informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))