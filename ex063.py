# 1-1-2-3-5-8-
n =  int(input('Digite o numero:'))
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
print('Fim')
