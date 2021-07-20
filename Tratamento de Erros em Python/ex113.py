n1 = n2 = 0
while True:
    try:
        n1 = int(input('Numero Inteiro: '))

        if n1 == int(n1):
            break
    except:
        print('\033[0:31mERRO .Valor invalido\033[m')


while True:
    try:
        n2 = float(input('Numero Real: '))
        if n2 == float(n2):
            break
    except:
        print('\033[0;31mERRO .Valor invalido\033[m')


print(f'Valores digitados inteiros {n1} e real {n2}')




