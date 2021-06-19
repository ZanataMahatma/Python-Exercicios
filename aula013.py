'''for c in range(0,100,5):
    print(c)
print('FIM')'''
'''
n1 = int(input('Digite um numero: '))
for c in range(0,n1+1):
    print(c)
print('FIM')'''

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s = s + n  # mesmo coisa que s += n
print('o Somatório de todos os valores foi {}'.format(s))