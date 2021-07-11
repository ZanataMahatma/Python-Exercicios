'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

#correção
matris = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matris[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matris[l][c]:^5}]', end='')
        if matris[l][c] % 2 ==0:
            spar = matris[l][c] + spar
    print()
for l in range (0,3):
    scol = matris[l][2] + scol
for c in range (0,3):
    if c == 0:
        mai = matris[1][c]
    elif matris[1][c] > mai:
        mai = matris[1][c]
print(f'O maior valor da segunda linha é {mai}')
print(f'A soma dos valores pares é {spar}')
print(f'A soma da terceira coluna é {scol}.')




# minha resposta
'''matris  = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somacoluna = 0
maior= 0
for l in range(0,3):
    for c in range(0,3):
        matris[l][c] =  int(input(f'Digite um valor para [{l},{c}]:'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matris[l][c]:^5}]',end='')
        if matris[l][c] % 2 ==0:
            soma = matris[l][c] + soma
        elif matris[l][c] != 0:
            somacoluna = matris[0][2] + matris[1][2] + matris [2][2]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma}')
print((f'A soma dos valores da terceira coluna é {somacoluna}'))
#print(f'A maior valor da segunda linha é {}')
'''
