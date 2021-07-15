'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
# minha resposta
'''from random import randint
r = 1
j = 0
countJ = 0
while r != j:
    j = int(input('Tente adivinhar !! de 1 a 10 :'))
    r = randint(1, 10)
    countJ = countJ + 1
    if r == j:
        print('\033[43mVocê ACERTOU\033[m')
        print('Computador escolheu: \033[33m{}\033[m'.format(r))
    else:
        print('Tente novamente')
        print('Computador escolheu \033[33m{}\033[m'.format(r))
print('Foram necessario {} JOGADAS PARA VC GANHAR'.format(countJ))'''

#correção
from random import randint
computador = randint(0,10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns'.format(palpite))