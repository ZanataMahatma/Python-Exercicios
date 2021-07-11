'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
 sabendo que o vencedor tirou o maior número no dado.'''
#correção
from random import randint
from time import sleep
from operator import itemgetter # biblioteca comando novo para  varrer o dicionario
jogo = {'jogador1': randint(1,6), # key=itemgetter(1))  vai selecionar os valores sorteados
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #  comando para deixa os jogadores em aordem e      reverse=True reverter
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'  {i+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)





# minha resposta incompleta
'''from random import randint
from time import sleep
cont = 0
jogador = dict()
for c in range (1,5):
    jogador['Jogador1'] = randint(1,10)
    jogador['Jogador2'] = randint(1,10)
    jogador['Jogador3'] = randint(1,10)
    jogador['Jogador5'] = randint(1,10)
for i,v in jogador.items():
    print(f'O {i} tirou {v}')
    sleep(1)
print('       Ranking dos Jogadores:')

for j in sorted(jogador.values()):
    print(f'O {j}')
    sleep(1)'''

