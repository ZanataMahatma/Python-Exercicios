'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

# minha solução
'''total = 0
count = -1
n = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    total = total + n
    count = count + 1
print('Você digitou {} números e a soma entre eles foi {}'.format(count,total - 999))'''


# correção
total = 0
count = -1
n = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    total = total + n
    count = count + 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(count,total))