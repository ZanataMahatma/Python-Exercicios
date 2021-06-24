r = 'S'
fat4 = 0
while r == 'S':
    n1 = int(input('Digite um numero: '))
    fat = n1 * 4
    fat2 = fat * 3
    fat3 = fat2 * 2
    fat4 = fat3 * 1
    print('{}x4x3x2x1={}'.format(n1,fat4))
    r = str(input('Quer Calcular outro numero fatorial? [S/N]')).upper()

print('Fim')