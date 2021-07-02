'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
# correção
from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os numeros sorteados foram: ',end='')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\nO NUMERO MAIOR SORTEADOR FOI: {max(numeros)}')
print(f'O NUMERO MENOR SORTEADO FOI: {min(numeros)}')


# minha resposta incompleta .
'''from random import choice
n1 = n2 = n3 = n4 =n5 = maior = menor = 0
tupla= (10,5,8,9,4)
if tupla != 0:
    n1 = choice(tupla)
    print(n1,end=' ')
    n2 = choice(tupla)
    print(n2,end=' ')
    n3 = choice(tupla)
    print(n3,end=' ')
    n4 = choice(tupla)
    print(n4,end=' ')
    n5 = choice(tupla)
    print(n5,)
elif n1 > n2:
        maior = n1
        if n3 < n2:
            maior = n1
        elif n4 < n3:
            maior = n1
        elif n5 < n4:
            maior = n1
else:
    menor = n2
print(tupla.index(maior))

'''