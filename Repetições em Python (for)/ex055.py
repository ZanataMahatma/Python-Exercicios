'''
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
pesomaior = 0
pesomenor = 0
for c in range(1,6):
    p = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        pesomaior = p
        pesomenor = p
    else:
        if p > pesomaior:
            pesomaior = p
        if p < pesomenor:
            pesomenor = p
print(' O maio peso lido foi de {}kg'.format(pesomaior))
print(' O menor peso lido foi de {}kg'.format(pesomenor))