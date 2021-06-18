'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
print('-='*20)
print('Analizador de Triângulos')
print('=-'*20)
r1 = float(input('Digite o Comprimento r1: '))
r2 = float(input('Digite o Comprimento r2: '))
r3 = float(input('Difite o Comprimento r3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA um triângulo ', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
'''
>>>>Triângulo Equilátero
são os triângulos que possuem as três medidas iguais
>>>>Triângulo isósceles
o triângulo isósceles possui dois lados
com medidas iguais e uma diferente, denominado de base.
>>>>Triângulo escaleno
o triângulo escaleno é
possua medidas diferentes em seus três lados
'''