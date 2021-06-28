'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120'''
#correção
'''from math import factorial
n =  int(input('Digite um numero para calcular seu FATORIAL:'))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n,f))'''


n =  int(input('Digite um numero para calcular seu FATORIAL:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))




#minha resposta
'''r = 'S'
fat4 = 0
while r == 'S':
    n1 = int(input('Digite um numero: '))
    fat = n1 * 4
    fat2 = fat * 3
    fat3 = fat2 * 2
    fat4 = fat3 * 1
    print('{}x4x3x2x1={}'.format(n1,fat4))
    r = str(input('Quer Calcular outro numero fatorial? [S/N]')).upper()

print('Fim')'''