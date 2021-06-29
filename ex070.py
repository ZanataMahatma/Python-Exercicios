print('=-' * 20)
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
print(f'O produto mais barato foi {nomeprod} que custa R${menor:.2f}')
