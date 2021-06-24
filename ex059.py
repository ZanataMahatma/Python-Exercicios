repete = 'SIM'
s = 0
while repete == 'SIM':
    n1 = int(input('Digite o Primeiro Valor:'))
    n2 = int(input('Digite o Segundo Valor'))
    s = int(input('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    Digite sua opção: '''))
    if s == 1:
        r = n1 + n2
        print('\nSoma escolhida:{}+{}={}'.format(n1,n2,r))
    elif s == 2:
        r = n1 * n2
        print('\n Multiplicação escolhida:{}x{}={}'.format(n1,n2,r))
    elif s == 3:
        if n1 > n2:
            print('Primeiro Valor digitado é maior {}'.format(n1))
        else:
            print('Segundo valor digitado é maior {}'.format(n2))
    elif s == 4:
        repete = 'SIM'
    else:
        repete = 'NÃO'

print('Fim do Programa')