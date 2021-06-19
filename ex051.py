n1 = int(input('Digite um Numero: '))
for c in range(1,10):
    r = n1 + (c - 1)*n1
    print('Termo da progressão {}'.format(r))
print('FIM')