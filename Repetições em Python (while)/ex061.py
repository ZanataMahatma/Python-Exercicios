'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

#correção
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo = termo + razão
    cont = cont + 1
print('fim')

# minha resposta
'''c = 0
n1 = 1
pa = 0
c = int(input('Digite o numero da PA:'))
while n1 < 10:
    pa = c * n1
    n1 = n1 + 1
    print('Termo da Progressão {}'.format(pa))

print('Fim')'''
