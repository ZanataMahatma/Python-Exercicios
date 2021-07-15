'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPA')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v = v + 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU')
            v=v+1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')




# minha resposta
'''from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPA')
print('-='*20)
perdeu = False
jogador = count = computador = 0
venceu = 0
while perdeu != True:
    computador = randint(1, 10)
    jogador = int(input('Diga um valor: '))
    pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    count =+ 1
    soma = jogador + computador
    resto = soma % 2
    if resto == 0:
        venceu = venceu + 1
        print('VOCÊ VENCEU!')
        print(f'Você jogou {jogador} e o computador {computador}.Total de {soma} deu PAR')
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
        perdeu = True
print('Você PERDEU!')
print('=-'*20)
print(f'GAME OVER! Você venceu {venceu} vezes.')
'''


