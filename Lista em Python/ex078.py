'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em
uma lista. No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista.
'''

#recapitulando
lista = []
maior = 0
menor = 0
for c in range (0,5):
    lista.append(int(input('Digite o Valor:')))
    if c == 0:
        maior = menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
print(f'Lista completa {lista}')
print(f'Maior numero da lista {maior} nas posições: ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f' {i}...',end='')
print() # para quebrar a linha
print(f'Menor numero da lista {menor} nas posições: ',end='')
for i ,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()# para quebrar a linha




















#correção
'''
listanum = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ',end='')
for i,v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for i,v in enumerate(listanum):
    if v == men:
        print(f'{i}...',end='')
print()
'''
# minha resposta
'''
lista = []
pos = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-'*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições {lista.index(max(lista))}...')
print(f'O menor valor digitado foi {min(lista)} nas posições {lista.index(min(lista))}...')
'''



