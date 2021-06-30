'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''



total = totamil = menor = cont =  0
barato = '' # C) nome do produto mais barato.
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço R$'))
    cont = cont + 1 # C) qual é o nome do produto mais barato.
    total = total + preço
    if preço > 1000:
        totamil = totamil + 1
    if cont == 1:     # C) qual é o nome do produto mais barato.
        menor = preço # C) qual é o nome do produto mais barato.
        barato = produto  # C) <--------------- nome do produto mais barato.
    else:             # C) qual é o nome do produto mais barato.
        if preço < menor: # C) qual é o nome do produto mais barato.
            menor = preço # C) qual é o nome do produto mais barato.
            barato = produto # C) <------------------ nome do produto mais barato.
    resp=' '
    while resp not in 'SN':
        resp= str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compra foi R${total:10.2f}')
print(f'Temos {totamil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}') # C) qual é o nome do produto mais barato.








# minha resposta
'''print('=-' * 20)
print('LOJA SUPER BARATÃO')
print('-=' * 20)
continuar = 'S'
produto = preço = maior = menor = total = nomeprod = count =0
while continuar == 'S':
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total = total + preço
    if preço > 1000:
        count = count + 1
    if preço != 0:
        maior = menor = preço
    else:
        if preço > maior:
            maior = preço
        if preço < menor:
            menor = preço
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {count} produtos custando mais de R$1000.0')
print(f'O produto mais barato foi {nomeprod} que custa R${menor:.2f}')'''
