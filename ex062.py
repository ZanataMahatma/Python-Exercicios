repete = 'S'
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
print('Fim{}'.format(a1))


