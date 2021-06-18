from random import randint
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
    print('Computador:{} Jogador:{} Jogador Ganha'.format('Pedra','Papel'))
elif computador == 2 and jogador == 3:
    print('Computador:{} Jogador:{} Jogador Ganha'.format('Papel','Tesoura'))
elif computador == 3 and jogador == 1:
    print('Computador:{} Jogador:{} Jogador Ganha'.format('Tesoura','Pedra'))
elif jogador == 1 and computador == 2:
    print('Computador:{} Jogador:{} Computador Ganha'.format('Papel','Pedra'))
elif jogador == 2 and computador == 3:
    print('Computador:{} Jogador:{} Computador Ganha'.format('Tesoura','Papel'))
else:
    jogador == 3 and computador == 1
    print('Computador:{} Jogador:{} Computador Ganha'.format('Pedra','Tesoura'))




