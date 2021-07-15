'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''
#correção
def ficha (jog='<Desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato')


#programa principal
n =str(input('Nome do jogador: '))
g =str(input('Numero de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)





# minha resposta
'''def ficha(a=0,b=0):
    if a == '':
        a = 'Desconhecido'
    print(f'O jogador {a} fez {b} gols(s) no campeonato.')





#programa principal
nome = str(input('Nome do jogador: '))
gols = int(input('Qtd_Gols: '))

ficha(nome,gols)'''

