somadosgols = 0
gols = list()
gerenciador= dict()
while True:
    gerenciador['Nome'] = str(input('Nome do Jogador: '))
    Partidas = int(input('Quantas Partidas? '))
    for i in range(Partidas):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    resp = str(input('Deseja continuar? [S/N]'))

    if resp in 'Nn':
        break

gerenciador['gols'] = gols
gerenciador['total'] = sum(gols)
for i,v in gerenciador.items():
    print(f'O campo {i} tem o valor {v}.')
print('-='* 30)
for i,v in enumerate(gols):
    print(f'=> Na partida {i}, fez {v} gols.')

