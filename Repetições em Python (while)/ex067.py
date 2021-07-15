'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário.
  O programa será interrompido quando o número solicitado for negativo.'''
# correção

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-='*30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-='*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# minha resposta
'''while True:
    count = 0
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    if n1 <= -1:
        break
    while count <= 9:
        count = count + 1
        tabuada = n1 * count
        print(f'{n1}x{count}={tabuada}')

print('PROGRAMA TABUADA ENCERRANDO. Volte sempre!')
'''
