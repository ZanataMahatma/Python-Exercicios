'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''

#cod correigido pelo professo guanabara
from random import randint
itens = ('Pedra','Papel','Tesoura') # tupla
computador = randint(0,2) # computador escolha aleatorio
print('''Sua Opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print('Computador jogou:\033[1;30;43m{}\033[m'.format(itens[computador])) # format pega os itens e randomiza para simular a jogada do computador
print('Jogador jogou: \033[1;30;43m{}\033[m'.format(itens[jogador]))
print('-='*11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:# compotador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:#computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

# minha resolução sem correção
'''from random import randint
print('-='*20)
print('Bem Vindo AO JOKENPÔ')
print('-='*20)
n1 = ['Pedra','papel','Tesoura']
computador = randint(1,3)

jogador = int(input('Escolha sua Jogada\n 1- Pedra\n 2- Papel\n 3- Tesoura\n Digite sua opção: '))
if jogador != 1 and jogador != 2 and jogador !=3:
    print('Jogada Invalida Tente Novamente!!!')
elif computador == jogador:
    print('EMPATE!!!')
elif computador == 1 and jogador == 2:
    print('Computador:{} \nJogador:{} \nJogador Ganha'.format('Pedra','Papel'))
elif computador == 2 and jogador == 3:
    print('Computador:{} \nJogador:{} \nJogador Ganha'.format('Papel','Tesoura'))
elif computador == 3 and jogador == 1:
    print('Computador:{} \nJogador:{} \nJogador Ganha'.format('Tesoura','Pedra'))
elif jogador == 1 and computador == 2:
    print('Computador:{} \nJogador:{} \nComputador Ganha'.format('Papel','Pedra'))
elif jogador == 2 and computador == 3:
    print('Computador:{} \nJogador:{} \nComputador Ganha'.format('Tesoura','Papel'))
else:
    jogador == 3 and computador == 1
    print('Computador:{}\n Jogador:{} \nComputador Ganha'.format('Pedra','Tesoura'))
'''

