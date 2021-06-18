import math
catop = float(input('Digite o Valor do Cateto oposto: '))
catad = float(input('Difite o Valor do Cateto Adjacente: '))
hipo = math.hypot(catop,catad)

print('Valor da Hipotenusa é {:.2f}'.format(hipo))
