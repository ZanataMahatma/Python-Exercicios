'''Exercício Python 62: Melhore o DESAFIO 61,
perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

#correção
print('Gerando uma PA')
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))

# MINHA RESPOSTA
'''repete = 'S'
c = 0
n1 = 0
pa = 0
a1 = 0
while repete == 'S':
    c = int(input('Digite o numero da PA:'))
    a1 = int(input('Quantos termos vc quer ? '))
    if a1 != 0:
        while n1 < a1:
            pa = c * n1
            n1 = n1 + 1
            print('Termo da Progressão {}'.format(pa))
    repete = str(input('Deseja continuar [S/N]?')).upper()
    while repete != 'S' and repete != 'N':
        repete = input('Comando inválido. Digite sim ou não: ').upper()
print('Fim{}'.format(a1))'''


