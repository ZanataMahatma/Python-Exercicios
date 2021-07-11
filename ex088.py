'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
#correção
from random import randint
from time import sleep
lista = []
jogos = list()
print('--'*20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('--'*20)
quant = int(input('Quantos jgos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont = cont +1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS','-=' * 3 )
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}:{l} ')
    sleep(1)



#minha resposta
'''from time import sleep
from random import sample
print('--'*20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('--'*20)
lista = list(range(1,60))
jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for c in range(jogos):
    n = sample(lista, 6)
    n.sort()
    print(n)
    sleep(1)
'''


