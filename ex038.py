n1 = int(input('Digite o Primeiro numero: '))
n2 = int(input('Digite o Segundo numero: '))
if n1 > n2:
    print('O numero {} é maior!!'.format(n1))
elif n2 > n1:
    print('O numero {} é maior !!'.format(n2))
elif n2 == n1:
    print( 'O primeiro NUMERO {} é igual ao segundo numero {}'.format(n1,n2))