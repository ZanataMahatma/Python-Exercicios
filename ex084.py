'''Exercício Python 084: Faça um programa que leia nome e peso de
várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

# minha resposta

temp = list()
dados = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:  # contar a lista de dados.
        maior = menor = temp[1]  #MAIOR E MENOR comando com IF
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor < temp[1]
    dados.append(temp[:])
    temp.clear()
    resp = str(input('Deseja Continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Ao todo,você cadastrou {len(dados)} pessoas')
print(f'O maior peso foi de {maior:.1f}kg.Peso de ',end='')
for i,v in enumerate(dados):
    if v[1] == maior:
        print(f'{v[0]}...')
print()
print(f'O menor peso foi de {menor:.1f}kg.Peso de ',end='')
for i,v in enumerate(dados):
    if v[1] == menor:
        print(f'{v[0]}...')
print()










'''dados = []
povo = []
peso = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    povo.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(povo)} pessoas')
print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de ', end='')
for p in povo:
    if p[1] == max(peso):
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {min(peso):.2f}Kg. Peso de ', end='')
for p in povo:
    if p[1] == min(peso):
        print(f'{p[0]} ', end='')'''