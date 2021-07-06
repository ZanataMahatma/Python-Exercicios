lista = ['Zanata',60],['Rodolfo',39],['Batman',40],['SuperMan',25]
maior = menor = count = 0
'''while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    count = count + 1
    resp = str((input('Deseja Coninuar ? [S/N] ')))
    if resp in 'Nn':
        break'''


for i,c in enumerate(lista):
    print(f'{i} {c[1]} ')

    if c == 0:
        maior = menor = c[1]
    elif c[1] > maior:
        maior = c[1]
    elif c[1] > menor:
        menor = c[1]

print(menor)
print(maior)

print(len(lista))


