'''Exercício Python 080: Crie um programa onde o usuário possa digitar
 cinco valores numéricos e cadastre-os em uma lista, já na posição correta
 de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista=[]

for c in range(0,5):
    num = int(input('Digite o Valor: '))
    if c == 0 or num > lista[-1]: # se o numero for mo primeiro numero ele faz entrada no numero
        lista.append(num)
        print('Adicionando ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos = pos + 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')


'''
lista_num = list()

for x in range(5):
    valor = int(input('Digite o valor: '))
    if x == 0:
        lista_num.append(valor)
        print(f'O número foi adicionado na posição {lista_num.index(valor)} da lista! ')
    else:
        for c in range(len(lista_num)):
            if valor <= lista_num[c]:
                lista_num.insert(c , valor)
                break
        if valor > lista_num[c]:
            lista_num.append(valor)
        print(f'O número foi adicionado na posição {lista_num.index(valor)} da lista! ')

print ('\n',lista_num)'''