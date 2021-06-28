'''Exercício Python 63: Escreva um programa que leia um número N inteiro
 qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:'''
#correção   0-1-1-2-3-5-8
print('-='*30)
print('Sequência de Fibonacci')
print('-='*30)
n = int(input('QUantos termos você quer mostrar ? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} - {}'.format(t1,t2),end='')
cont=3
while cont <= n:
    t3 = t1 + t2
    print('- {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('- FIM')









# minha solução 1-1-2-3-5-8-
'''n =  int(input('Digite o numero:'))
n2 = 0
n3 = 0
r = 'S'
while r == 'S':
    n = int(input('Digite: '))
    while n > n2:
        n2 = n2 + 1
        n3 = n3 + 1
        n = n2 + n3
        print('{}{}{}'.format(n,n2,n3))

    r = str(input('Sair  [S/N]')).upper()
print('Fim') '''
