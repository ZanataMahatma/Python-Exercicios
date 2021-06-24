r = 'N'
c = 1
count = 1
pa = 0
A = 10


while count < A or r == 'S':
    c = int(input('Digite o numero da PA:'))
    pa = c * count
    count = count + 1
    print('Termo da Progressão {}'.format(pa))
    if count == A:
        A = A + 10
        count = 0
        r = str(input('Deseja continuar [S/N]? ')).upper().strip()

print('Fim')

