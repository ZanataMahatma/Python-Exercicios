'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.'''

#correção
matrix = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()



# minha resposta
'''lista1 = list()
lista2 = list()
lista3 = list()
for c in range(0,3):
    lista1.append(int(input(f'Digite um valor [0, {c}]:')))
for p in range(0,3):
    lista2.append(int(input(f'Digite um valor [1, {p}]:')))
for n in range(0,3):
    lista3.append(int(input(f'Digite um valor [2, {n}]:')))
print(f'{lista1}\n{lista2}\n{lista3}')'''




